#!/usr/bin/python3

"""
Module to perfom simple queries on the model_state model
using and ORM - SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, dbase: str) -> None:

    """
    Connect to the database and make queries using ORM
    """
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(user, passwd, dbase))
        Session = sessionmaker(bind=engine)
        state_session = Session()

        lousiana = State(name="Louisiana")
        state_session.add(lousiana)
        state_session.commit()
        print(lousiana.id)
    except Exception as e:
        return e


if __name__ == "__main__":
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
