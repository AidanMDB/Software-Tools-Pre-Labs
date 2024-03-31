

from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column


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
        self.emailID = f"{self.lastName.lower()}.{self.firstName[0].lower()}@university.com"

    def __repr__(self) -> str:
        return f"Student(fname={self.firstName!r}, lname={self.lastName!r}, id={self.studentID!r}, email={self.emailID!r})"


def create_table(engine):
    Base.metadata.create_all(engine)


if __name__ == "__main__":

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///database.db", echo=True)
    create_table(engine)
