from database import Base, engine
from graph import graph
from queries import queries

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    queries()
    graph()
