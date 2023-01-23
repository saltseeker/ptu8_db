from model import Project, engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

def user_choice_menu():
    print("===[ Project Management System ]===")
    print("1 | add a new project")
    print("2 | list/search projects")
    print("3 | update a project")
    print("4 | delete a project")
    print("0 | exit")
    choice = input("Make a choice: ")
    return choice

def add_project(name, price):
    project = Project(name, price)
    session.add(project)
    session.commit()
    print(project)
    return project

def insert_project_from_input():
    try:
        name = input("Name: ")
        price = float(input("Price: "))
    except ValueError:
        print("Error: Price must be a number")
    else:
        return add_project(name, price)

def list_projects(query=session.query(Project)):
    if query and len(query.all()) > 0:
        for project in query.all():
            print(project)
    else:
        print("--- No Projects Found ---")

def search_projects(query=session.query(Project)):
    search = input("Search or enter nothing to continue: ")
    if not search:
        return
    try:
        query_price = float(search)
    except ValueError:
        query = list_projects(query.filter(Project.name.ilike(f"%{search}%")))
    else:
        query = list_projects(query.filter(Project.price >= query_price))
    finally:
        search_projects(query or session.query(Project))

while True:
    choice = user_choice_menu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        insert_project_from_input()
    elif choice == "2":
        list_projects()
        search_projects()
    else:
        print(f"Error: wrong choice {choice}")
