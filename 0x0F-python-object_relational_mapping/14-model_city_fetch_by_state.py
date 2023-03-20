#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from venv import create
from sqlalchemy import create_engine, true
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for city, state in session.query(City, State)\
        .filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
