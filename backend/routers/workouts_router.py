from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/workouts"
)

@router.get("")
def index() :
    return Response("Hello from the workouts router!")

@router.get("/create-workout-plan")
def index() :
    return Response("Creating workout plan!")