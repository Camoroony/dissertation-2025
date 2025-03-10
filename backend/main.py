from fastapi import FastAPI, Response
from backend.routers.users_router import router as users_router
from backend.routers.workouts_router import router as workouts_router

app = FastAPI()

app.include_router(users_router)
app.include_router(workouts_router)

@app.get("/")
def index() :
    return Response("Backend API is running.")