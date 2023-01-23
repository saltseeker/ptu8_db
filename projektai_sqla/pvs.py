from model import Project, engine
from sqlalchemy.orm import sessionmaker


sessionmaker = sessionmaker(bind=engine)()