#!/usr/bin/python3
"""
Defines the state model, containing the State class and
"""
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """
    State class
        id -> state.id
        name -> state.name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "{}: {}".format(self.id, self.name)
