from colanderalchemy import setup_schema
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):
    """A project model

    Attributes:
        id (int): ID
        name (str): Title
    """
    __tablename__ = 'projects'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)


setup_schema(None, Project)
