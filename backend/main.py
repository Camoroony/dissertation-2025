from fastapi import FastAPI, Response
from routers.users import router as users_router
from routers.workouts import router as workouts_router

app = FastAPI()

app.include_router(users_router)
app.include_router(workouts_router)

@app.get("/")
def index() :
    return Response("Backend API is running.")