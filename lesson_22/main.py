from db.base import SessionLocal, engine, Base
from db.models.user import User
from db.models.student import Student
from db.models.course import Course
import random


try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except Exception as e:
    print(f"An error occurred while creating tables: {e}")


def add_user(name, age):
    session = SessionLocal()
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    session.close()

def add_student(name):
    session = SessionLocal()
    new_student = Student(name=name)
    session.add(new_student)
    session.commit()
    session.close()

def add_course(title):
    session = SessionLocal()
    new_course = Course(title=title)
    session.add(new_course)
    session.commit()
    session.close()

def enroll_student_to_course(student_id, course_id):
    session = SessionLocal()
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)
    if student and course:
        student.courses.append(course)
        session.commit()
    session.close()

def update_student(student_id, new_name):
    session = SessionLocal()
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
    session.close()

def update_course(course_id, new_title):
    session = SessionLocal()
    course = session.get(Course, course_id)
    if course:
        course.title = new_title
        session.commit()
    session.close()

def delete_student(student_id):
    session = SessionLocal()
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
    session.close()


def create_courses_and_enroll_students(num_courses=5, num_students=20):
    session = SessionLocal()

    courses = [Course(title=f'Course {i + 1}') for i in range(num_courses)]
    session.add_all(courses)
    session.commit()

    students = [Student(name=f'Student {i + 1}') for i in range(num_students)]
    session.add_all(students)
    session.commit()

    for student in students:
        random_courses = random.sample(courses, k=random.randint(1, num_courses))
        student.courses.extend(random_courses)

    session.commit()
    session.close()


add_user("John Uik", "25")
add_student("Messi")
add_course("Bob 101")
enroll_student_to_course(1, 1)

create_courses_and_enroll_students()

update_student(1, "Messi Smith")


update_course(1, "Mathematics 101")


delete_student(1)