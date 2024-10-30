from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from .association import student_course_table


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    students = relationship("Student", secondary=student_course_table, back_populates="courses")
