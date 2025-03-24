from fastapi import FastAPI, Response
from routers.users_router import router as users_router
from routers.workouts_router import router as workouts_router
from routers.chatbot_router import router as chatbot_router
from database.sql.init_sql_db import create_db
from database.mongodb.references_init import references_init

app = FastAPI()

app.include_router(users_router)
app.include_router(workouts_router)
app.include_router(chatbot_router)

create_db()

mongodb_references_state = references_init()

if mongodb_references_state == True:
    print("Added application references to MongoDB instance.")

@app.get("/")
def index() :
    return Response("Backend API is running.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)