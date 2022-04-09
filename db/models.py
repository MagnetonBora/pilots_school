from faker import Faker
from pesel import Pesel
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(32), nullable=False)
    address = Column(String(64))

    # student_g = relationship("StudentGrade", back_populates="id_student")

    def __repr__(self):
        return f"Student({self.id}, {self.first_name}, {self.last_name}, {self.phone})"

    @staticmethod
    def create_fake_student():
        fake = Faker()
        return Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            pesel=Pesel.generate(),
            phone=fake.phone_number(),
            address=fake.address()
        )


def create_fake_users(session, count=50):
    student_generated = 0
    while student_generated < count:
        try:
            session.add(Student.create_fake_student())
            session.commit()
        except IntegrityError:
            session.rollback()
            continue
        student_generated += 1
