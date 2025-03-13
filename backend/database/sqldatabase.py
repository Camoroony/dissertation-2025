import os
from sqlmodel import SQLModel, create_engine, Session

SQLDB_URL = os.getenv("SQLDB_URL", "mysql+pymysql://root:P4$$w0Rd16@127.0.0.1:3306/hypertrophy_db")

engine = create_engine(SQLDB_URL, echo=True)

def create_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully.")

def get_db_session():
    with Session(engine) as session:
        yield session
