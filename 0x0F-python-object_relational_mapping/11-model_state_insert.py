#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database
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

    add_state = State(name="Louisiana")
    session.add(add_state)
    # commit and close session
    session.commit()
    print(add_state.id)
    session.close()