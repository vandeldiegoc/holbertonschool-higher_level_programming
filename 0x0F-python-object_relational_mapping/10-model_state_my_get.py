#!/usr/bin/python3
"""query table in databases
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    line = session.query(State).order_by(State.id.asc()) \
        .filter_by(name=sys.argv[4]).first()
    if not line:
        print("Not found")
    else:
        print("{}".format(line.id))
