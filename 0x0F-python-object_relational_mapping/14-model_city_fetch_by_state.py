#!/usr/bin/python3
"""
Script that prints all City objects
from the database hbtn_0e_14_usa
"""
if __name__ == "__main__":
    """ This won't be run when imported """

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    city_objects = (session.query(City, State).join(State).
                    order_by(City.id))

    for city_object, state_object in city_objects:
        print("{}: ({}) {}".format(state_object.name, city_object.id,
                                   city_object.name))

    session.close()
