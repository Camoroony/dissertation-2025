from fastapi import APIRouter, Response, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session
from models.input_models import WorkoutGenInput
from models.db_models import UserSQL
from models.utilities.sql_serialising import serialise_workout_plan, serialise_workout_session, serialise_exercise
from models.utilities.csv_exporter import export_workout_plan_csv
from security.jwt_token import verify_token
from database.sql.init_sql_db import get_db_session
from database.sql.workout_plan_db import add_workout_plan, delete_workout_plan, get_workout_plan, get_workout_plans, get_workout_plans_by_user
from database.sql.workout_session_db import get_workout_session
from database.sql.exercise_db import get_exercise
from database.mongodb.workout_context_db import add_workout_context, get_workout_context, get_workout_sources_used, delete_workout_context
from database.mongodb.chat_history_db import create_chat_history, delete_chat_history_by_workoutplan
from ai_services.gen_workout_plan import generate_workout_plan
from ai_services.gen_workout_info import generate_exercise_overview, generate_workoutsession_overview
import io

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")


@router.post("/create-workout-plan", status_code=201)
def create_workout_plan(workout_input: WorkoutGenInput, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    ai_response_data = generate_workout_plan(workout_input)

    add_result_sql = add_workout_plan(ai_response_data["response"], user.id, db)

    add_workout_context(add_result_sql.id, ai_response_data["context"], list(ai_response_data["sources_used"]))

    create_chat_history(user.id, "Workout", add_result_sql)

    return {"id": add_result_sql.id}

@router.get("/get-workout-plan")
def get_workout(id: int, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    try:
     workoutplan = get_workout_plan(id, user.id, db)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occured retrieving the workout plan.")
         
    if not workoutplan:
        raise HTTPException(status_code=400, detail=f"Error with retrieving workout plan Id: {id} not found")
    
    workoutplan_read = serialise_workout_plan(workoutplan)

    return workoutplan_read

@router.get("/get-workout-plans")
def get_all_workouts(user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
        raise HTTPException(f"User Token verification failed")

    try:
     workoutplans = get_workout_plans(db)

     serialised_workout_plans = []

     for workoutplan in workoutplans:
       serialised_workout_plan = serialise_workout_plan(workoutplan)
       serialised_workout_plans.append(serialised_workout_plan)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occured when retrieving workout plans.")
         
    if not workoutplans:
        raise HTTPException(status_code=400, detail="Error with retrieving workout plans: workout plans not found")

    return serialised_workout_plans


@router.get("/export-workout-plan-csv")
def get_workout_csv(id: int, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
        raise HTTPException(f"User Token verification failed")
    
    try:
     workoutplan = get_workout_plan(id, user.id, db)
     serialised_workoutplan = serialise_workout_plan(workoutplan)

     csvfile = export_workout_plan_csv(serialised_workoutplan)

     csvfile.seek(0)
     csv_bytes = io.BytesIO(csvfile.read().encode("utf-8"))

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occured retrieving the workout plan.")
     
    if not workoutplan:
        raise HTTPException(status_code=400, detail=f"Error with retrieving workout plan Id: {id} not found")

    return StreamingResponse(
        csv_bytes,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=workout_plan.csv"}
    )

@router.get("/get-workout-plans-by-user")
def get_workout_plan_by_userid(user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
        raise HTTPException(f"User Token verification failed")

    try:
     workoutplans = get_workout_plans_by_user(user.id, db)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured retrieving the workout plans for user: {user.id}.")

    return workoutplans

@router.get("/get-workout-plan-sources", status_code=200)
def get_workout_plan_sources(id: int, user: UserSQL = Depends(verify_token)) :

    if not user:
      raise HTTPException(f"User Token verification failed")

    try:
     sources_used = get_workout_sources_used(id) 

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occured retrieving the workout plans for user: {user.id}.")
         
    if not sources_used:
        raise HTTPException(status_code=400, detail=f"Error with retrieving workout plans for user Id: {user.id}")
    
    return sources_used


@router.delete("/delete-workout-plan")
def delete_workout(workout_plan_id: int, db: Session = Depends(get_db_session)) :

    delete_result_sql = delete_workout_plan(workout_plan_id, db)

    delete_result_mongodb = delete_workout_context(workout_plan_id)

    delete_chathistory_result_mongodb = delete_chat_history_by_workoutplan(workout_plan_id)

    if delete_result_sql is False:
        raise HTTPException(status_code=400, detail=f"Error with deleting workout plan Id: {workout_plan_id}")
    
    if delete_result_mongodb is False:
        raise HTTPException(status_code=400, detail=f"Error with deleting workout context for workout Id: {workout_plan_id}")
    
    if delete_chathistory_result_mongodb is False:
        raise HTTPException(status_code=400, detail=f"Error with deleting workout plan chat history for workout Id: {workout_plan_id}")

    return Response(
        f"Deleted workout plan (Id: {workout_plan_id})\n"
        f"Deleted workout context (Id: {delete_result_mongodb})",
        status_code=200
    )


@router.get("/get-workoutsession-info", status_code=200)
def get_workoutsession_info(id: int, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    workout_session = get_workout_session(id, db)
    workout_session_dict = serialise_workout_session(workout_session)

    workout_plan = get_workout_plan(workout_session.workoutplan_id, user.id, db)
    workout_plan_dict = serialise_workout_plan(workout_plan)

    context = get_workout_context(workout_session.workoutplan_id)

    ai_response_data = generate_workoutsession_overview(context, workout_plan_dict, workout_session_dict)

    return ai_response_data


@router.get("/get-exercise-info", status_code=200)
def get_exercise_info(id: int, user: UserSQL = Depends(verify_token), db: Session = Depends(get_db_session)) :

    if not user:
        raise HTTPException(f"User Token verification failed")

    exercise = get_exercise(id, db)

    if not exercise:
        raise HTTPException(f"No exercise found with the Id: {id}")

    exercise_dict = serialise_exercise(exercise)

    ai_response_data = generate_exercise_overview(exercise_dict["exercise_name"])

    return ai_response_data