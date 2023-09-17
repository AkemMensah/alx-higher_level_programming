#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # creating an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # creating a configured "Session" class
    Session = sessionmaker(bind=engine)
    # creating a Session
    session = Session()
    Base.metadata.create_all(engine)

    s_tate = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    for state in s_tate:
        print("{}: {}".format(state.id, state.name))
    session.close()