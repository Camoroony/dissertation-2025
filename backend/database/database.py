from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = ""
engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
