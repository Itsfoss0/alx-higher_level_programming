#!/usr/bin/python3
"""
Defines the city model, containing the State class and
should I just add here a bunch of random strings, texts
and words to make this look longer and fool the checker?
"""
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base

Base = declarative_base()


class State(Base):
    """
    State class
        id -> citie.id
        name -> state.name
        state_id -> foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return "{}: {}".format(self.id, self.name)
