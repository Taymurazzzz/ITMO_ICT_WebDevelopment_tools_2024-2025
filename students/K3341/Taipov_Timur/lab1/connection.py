from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv
import os
load_dotenv()

db_url = os.getenv("DB_URL")
engine = create_engine(db_url)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session