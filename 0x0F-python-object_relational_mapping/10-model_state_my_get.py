#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    """ This won't be run when imported """

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state_matches_name = session.query(State).filter(
        argv[4] == State.name).first()

    if state_matches_name:
        print("{}".format(state_matches_name.id))
    else:
        print("Not found")

    session.close()
