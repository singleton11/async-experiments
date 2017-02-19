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
    title: str = Column(String)


def upgrade(migrate_engine):
    """Create projects table"""
    Project.__table__.create(migrate_engine)


def downgrade(migrate_engine):
    """Drop projects table"""
    Project.__table__.drop(migrate_engine)
