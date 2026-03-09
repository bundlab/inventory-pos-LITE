from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from app.core.config import settings

connect_args = {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

async_engine = create_async_engine(settings.DATABASE_URL)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

def get_session() -> Session:
    with engine.connect() as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
