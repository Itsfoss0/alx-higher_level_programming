#!/usr/bin/python3

from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base

engine = create_engine('mysql+mysqldb://root:root@localhost/states', echo=True)
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "[State]: {} of id {}".format(self.name, self.id)
