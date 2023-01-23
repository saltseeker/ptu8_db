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
        query = query.filter(Project.name.ilike(f"%{search}%"))
    else:
        query = query.filter(Project.price >= query_price)
    finally:
        list_projects(query)
        if len(query.all()) > 0:
            search_projects(query)
        else:
            search_projects()

def delete_project(project):
    print(f"Deleting project {project.id}...")
    session.delete(project)
    session.commit()

def get_project_by_id():
    list_projects()
    try:
        id = int(input("Enter project ID: "))
    except ValueError:
        print("Error: ID must be a number")
    else:
        return session.query(Project).get(id)

def update_project(project, **changes):
    for column, value in changes.items():
        if value:
            setattr(project, column, value)
    session.commit()
    print(project)

def collect_changes(project):
    print(project)
    print("Enter new values or nothing to leave existing.")
    changes = {
        "name": input("Name: "),
        "price": input("Price: "),
    }
    return changes

while True:
    choice = user_choice_menu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        insert_project_from_input()
    elif choice == "2":
        list_projects()
        search_projects()
    elif choice == "3":
        project = get_project_by_id()
        update_project(project, **collect_changes(project))
    elif choice == "4":
        delete_project(get_project_by_id())
    else:
        print(f"Error: wrong choice {choice}")
