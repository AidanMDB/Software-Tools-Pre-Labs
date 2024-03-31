# ######################################################
# Author :  Aidan Dannhausen-Brun
# email :   adannhau@purdue.edu
# ID :      ee364a10
# Date :    3/31/24
# ######################################################


from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


class Base(DeclarativeBase):
    pass


class Student(Base):

    __tablename__ = "students"

    firstName = Column("first_name", String)
    lastName = Column("last_name", String)
    studentID = Column("id", Integer, primary_key=True)
    emailID = Column("email", String)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.emailID = f"""{self.lastName.lower()}.
                            {self.firstName[0].lower()}@university.com"""

    def __repr__(self) -> str:
        return f"""Student(fname={self.firstName!r}, lname={self.lastName!r},
                    id={self.studentID!r}, email={self.emailID!r})"""


def create_table(engine):
    Base.metadata.create_all(engine)


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///database.db", echo=True)
    create_table(engine)
