from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data/projektai.db')
Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.price}, {self.created_at})"

    def __str__(self):
        return f"ID {self.id}: {self.name}, kainuojantis {self.price}, sukurtas {self.created_at}"


if __name__ == '__main__':
    Base.metadata.create_all(engine)
