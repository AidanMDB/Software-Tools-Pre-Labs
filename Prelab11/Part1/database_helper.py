# ######################################################
# Author :  Aidan Dannhausen-Brun
# email :   adannhau@purdue.edu
# ID :      ee364a10
# Date :    3/31/24
# ######################################################

# from gcloud_connector import connect_with_connector
from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine
from student import Student, create_table

GCLOUD_MODE = False

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


def create_local_engine():
    engine = create_engine("sqlite:///database.db", echo=True)
    return engine


def insertStudent(engine, student1: Student):
    """Inserts a new student in the table"""
    with Session(engine) as session:
        session.add(student1)
        session.commit()


def getStudentsByName(engine, lastname: str):
    """Returns all rows with last name matching lastname"""
    with Session(engine) as session:
        stmt = select(Student).where(Student.lastName == lastname)
        results = session.execute(stmt).fetchall()
        print("Student results: ", results)


def updateID(engine, student1: Student, ID: int):
    """Updates the ID of the row containing the student details in the
    database"""
    with Session(engine) as session:
        stmt = select(Student).where(Student.studentID == ID)
        idExists = session.scalars(stmt).fetchall()

        if len(idExists):
            raise Exception("This ID is already being used")

        session.add(student1)
        # stmt = select(Student).where(Student.studentID == student1.studentID)
        # student = session.scalars(stmt).first()
        student1.studentID = ID

        session.commit()


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":

    engine = create_local_engine()
    create_table(engine)

    aidan = Student(
        firstName="Aidan",
        lastName="DB",
        studentID=123456
    )

    bob = Student(
        firstName="bob",
        lastName="smith",
        studentID=0
    )

    insertStudent(engine, aidan)
    insertStudent(engine, bob)
    getStudentsByName(engine, "smith")
    updateID(engine, bob, 1008349)
    getStudentsByName(engine, "smith")
