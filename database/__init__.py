"""
Package with database layer for the sample app.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .model import Entity

engine = create_engine("sqlite+pysqlite:///:memory:")
Session = sessionmaker(bind=engine)


def create_tables() -> None:
    """
    Method for creating all tables in the database.
    """
    Entity().metadata.create_all(engine)
