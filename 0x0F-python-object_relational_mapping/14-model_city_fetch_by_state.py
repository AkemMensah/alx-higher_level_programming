#!/usr/bin/python3
"""
A script that prints all City objects from the database
"""
from model_city import City
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

    city = session.query(State, City).join(City).order_by(City.id)
    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Close session
    session.close()