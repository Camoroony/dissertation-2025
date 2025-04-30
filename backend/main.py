from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from routers.users_router import router as users_router
from routers.workouts_router import router as workouts_router
from routers.chatbot_router import router as chatbot_router
from routers.ratings_router import router as ratings_router
from routers.references_router import router as references_router
from database.init_seed import seed_dummy_data
from database.sql.init_sql_db import create_db
from database.mongodb.references_db import references_init
from database.chroma.init_chroma_db import init_vectorstores

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(users_router)
app.include_router(workouts_router)
app.include_router(chatbot_router)
app.include_router(ratings_router)
app.include_router(references_router)

create_db()
seed_dummy_data()
references_init()
init_vectorstores()

@app.get("/")
def index() :
    return Response("Backend API is running.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)