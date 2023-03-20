#!/usr/bin/python3
"""
Connect to a database and perform some queries
using an ORM - SQLAlchemy
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State


def connect_and_query(user: str, passwd: str, dbase: str) -> None:
    try:
        engine = create_engine('mysql+mysqldb://{}:{}/{}'
                               .format(user, passwd, dbase))
        Session = sessionmaker(bind=engine)

        _session = Session()
        for city, state in _session.query(City, State).filter(
                    City.state_id == State.id).order_by(City.id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    except Exception as e:
        return e


if __name__ == "__main__":
    connect_and_query(sys.argv[1], sys.argv[2], sys.argv[3])
