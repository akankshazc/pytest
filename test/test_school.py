import pytest
from pytest import mark, raises

from source.school import *

# Pytest Fixtures


@pytest.fixture
def harry_potter():
    return Student("Harry Potter")


@pytest.fixture
def hermione_granger():
    return Student("Hermione Granger")


@pytest.fixture
def ron_weasley():
    return Student("Ron Weasley")


@pytest.fixture
def dumbledore():
    return Teacher("Albus Dumbledore")


@pytest.fixture
def snape():
    return Teacher("Severus Snape")


@pytest.fixture
def defense_against_dark_arts_class(dumbledore, harry_potter, hermione_granger, ron_weasley):
    students = [harry_potter, hermione_granger, ron_weasley]
    return Classroom(dumbledore, students, "Defense Against the Dark Arts")


@pytest.fixture
def potions_class(snape, harry_potter, hermione_granger):
    students = [harry_potter, hermione_granger]
    return Classroom(snape, students, "Potions")


# Test cases for the Classroom functionality
def test_initial_classroom_setup(defense_against_dark_arts_class):
    classroom = defense_against_dark_arts_class
    assert classroom.teacher.name == "Albus Dumbledore"
    assert len(classroom.students) == 3
    assert classroom.course_title == "Defense Against the Dark Arts"


def test_add_student(defense_against_dark_arts_class, ron_weasley):
    classroom = defense_against_dark_arts_class
    new_student = ron_weasley
    classroom.add_student(new_student)
    assert len(classroom.students) == 4
    assert new_student in classroom.students


def test_add_student_too_many(defense_against_dark_arts_class):
    classroom = defense_against_dark_arts_class
    # Fill classroom to max capacity of 10
    for i in range(7):  # Adding 7 more students
        classroom.add_student(Student(f"Student {i+4}"))
    with raises(TooManyStudents):
        classroom.add_student(Student("New Student"))


def test_remove_student(defense_against_dark_arts_class):
    classroom = defense_against_dark_arts_class
    student_to_remove = "Harry Potter"
    classroom.remove_students(student_to_remove)
    assert len(classroom.students) == 2
    assert not any(
        student.name == student_to_remove for student in classroom.students)


def test_change_teacher(defense_against_dark_arts_class, snape):
    classroom = defense_against_dark_arts_class
    new_teacher = snape
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Severus Snape"

# Parametrized test for adding multiple students


@mark.parametrize("student_name", ["Luna Lovegood", "Neville Longbottom", "Ginny Weasley", "Fred Weasley"])
def test_add_multiple_students(defense_against_dark_arts_class, student_name):
    classroom = defense_against_dark_arts_class
    new_student = Student(student_name)
    classroom.add_student(new_student)
    assert len(classroom.students) > 3
    assert new_student.name == student_name
    assert new_student in classroom.students

# Test case where the classroom can add students up to capacity (10)


def test_add_up_to_capacity():
    teacher = Teacher("Minerva McGonagall")
    students = [Student(f"Student {i+1}") for i in range(9)]
    classroom = Classroom(teacher, students, "Transfiguration")

    # Try adding 10th student (should succeed)
    new_student = Student("Student 10")
    classroom.add_student(new_student)
    assert len(classroom.students) == 10

    # Try adding 11th student (should raise TooManyStudents)
    with raises(TooManyStudents):
        classroom.add_student(Student("Student 11"))
