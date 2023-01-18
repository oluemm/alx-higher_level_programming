#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /<database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    USER = sys.argv[1]
    PASSWORD = sys.argv[2]
    DB_NAME = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(USER, PASSWORD, DB_NAME),
        pool_pre_ping=True  # It checks if the connection is
        # still alive and re-connects if not.
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in (
        session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    ):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
