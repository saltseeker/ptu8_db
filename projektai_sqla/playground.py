from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from model import Project

engine = create_engine("sqlite:///data/projektai.db")
# Session = sessionmaker(bind=engine)
# Session = Session()
session = sessionmaker(bind=engine)()

#CRUD = Create Read Update Delete
#Create
# naujas_projektas = Project("Kazkas naujo", 14000)
# kitas_projektas = Project("Kiti reikalai", 500)
# session.add(naujas_projektas)
# session.add(kitas_projektas)

#Read
# projektas1 = session.query(Project).get(2)
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
# projektai = session.query(Project).all()


# pigus_projectai = session.query(Project).filter_by(Project.price <= 10000).all()
# print(pigus_projectai)

# reikalai = session.query(Project).filter(Project.name.ilike("%kal%")).all()
# print(reikalai)

#Update
# brangus = session.query(Project).filter(Project.price > 1000).first()
# brangus.price = 1000
# session.commit()
# print(brangus)


#Delete
# projektas2 = session.query(Project).filter_by(name="Kiti reikalai").one()
# session.delete(projektas2)
# session.commit()
# projektai = session.query(Project).all()
# print(projektai)
