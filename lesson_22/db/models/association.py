from sqlalchemy import Table, Column, Integer, ForeignKey
from ..base import Base

student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)
