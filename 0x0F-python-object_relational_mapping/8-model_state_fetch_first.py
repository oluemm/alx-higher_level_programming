#!/usr/bin/env python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql username> /
                                      <mysql password> /
                                      <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

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

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
