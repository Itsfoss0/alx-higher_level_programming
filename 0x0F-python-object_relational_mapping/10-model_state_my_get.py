#!/usr/bin/python3

"""
Module to perfom simple queries on the model_state model
using an ORM - SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def connect_and_query(user: str, passwd: str, dbase: str, search: str) -> None:

    """
    Connect to the database and make queries using ORM
    Args:
        user (str): mysql user
        passwd (str): mysql password for `user`
        dbase (str): Database to use
        search (str): State to search for
    """
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(user, passwd, dbase))
        Session = sessionmaker(bind=engine)
        state_session = Session()
        states = state_session.query(State).order_by(State.id).all()

        for state in states:
            if state.name == search:
                print(state.id)
                break
        else:
            print("Not found")
    except Exception as e:
        return e


if __name__ == "__main__":
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
