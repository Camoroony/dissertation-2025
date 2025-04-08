from fastapi import APIRouter, Response, Depends, HTTPException
from sqlmodel import Session
from models.input_models import WorkoutGenInput
from models.utilities.sql_seralising import serialise_exercise
from database.sql.init_sql_db import get_db_session
from database.sql.workout_plan_db import add_workout_plan, delete_workout_plan
from database.sql.exercise_db import get_exercise
from database.mongodb.workout_context_db import add_workout_context, get_workout_context, delete_workout_context
from ai_services.gen_workout_plan import generate_workout_plan
from ai_services.gen_workout_info import generate_exercise_overview, generate_workoutsession_overview

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")


@router.post("/create-workout-plan")
def create_workout(workout_input: WorkoutGenInput, user_id: int, db: Session = Depends(get_db_session)) :

    ai_response_data = generate_workout_plan(workout_input)

    add_result_sql = add_workout_plan(ai_response_data["response"], user_id, db)

    add_result_mongodb = add_workout_context(add_result_sql.id, ai_response_data["context"], list(ai_response_data["sources_used"]))

    return Response(
        f"Created workout plan Id: {add_result_sql.id} for user: {add_result_sql.user_id}\n"
        f"Workout context added, Id: {add_result_mongodb['inserted_id']}\n"
        f"Sources analysed during plan creation: {ai_response_data['sources_used']}",
        status_code=200
    )


@router.delete("/delete-workout-plan")
def delete_workout(workout_plan_id: int, db: Session = Depends(get_db_session)) :

    delete_result_sql = delete_workout_plan(workout_plan_id, db)

    delete_result_mongodb = delete_workout_context(workout_plan_id)

    if delete_result_sql is False:
        raise HTTPException(status_code=400, detail=f"Error with deleting workout plan Id: {workout_plan_id}")
    
    if delete_result_mongodb is False:
        raise HTTPException(status_code=400, detail=f"Error with deleting workout context for workout Id: {workout_plan_id}")

    return Response(
        f"Deleted workout plan (Id: {workout_plan_id})\n"
        f"Deleted workout context (Id: {delete_result_mongodb})",
        status_code=200
    )


@router.get("/get-workoutsession-info")
def get_workoutsession_info(workout_plan_id: int, workoutsession_id: int) :

    context = get_workout_context(workout_plan_id)

    ai_response_data = generate_workoutsession_overview(context, workoutsession_id)

    return Response(ai_response_data, status_code=200)


@router.get("/get-exercise-info")
def get_exercise_info(exercise_id: int, db: Session = Depends(get_db_session)) :

    exercise = get_exercise(exercise_id, db)

    if not exercise:
        raise HTTPException(f"No exercise found with the Id: {exercise_id}")

    exercise_dict = serialise_exercise(exercise)

    ai_response_data = generate_exercise_overview(exercise_dict["exercise_name"])

    return ai_response_data