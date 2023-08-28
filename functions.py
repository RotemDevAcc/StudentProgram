import random
from enum import Enum
from app import Student
def AddStudent(students):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    id_number = GetRandomID()
    

    student = Student(first_name, last_name, id_number)
    students.append(student)
    print(f"Student {student.GetFullName()} added with ID: {id_number}")


def GetRandomID():
    randomid = random.randint(210000000,450000000)
    return str(randomid)

def FindStudent(students):
    id_number = input("Enter ID Number: ")
    for student in students:
        if(student.identifier == id_number):
            return student
        
    return None
    
def PrintAllStudents(students):
    for student in students:
        print(type(student))

def PrintActions(actions):
    for action in actions:
        print(f"{action.name} - {action.value}")

class EditActions(Enum):
    ADDTEST = 1
    LISTTESTS = 2

def EditStudent(student):
    for action in EditActions:
        print(f"{action.name} - {action.value}")

    action = EditActions(int(input(f"Choose Your Action For {student.GetFullName()}: ")))

    if(action == EditActions.ADDTEST):
        type = input("Test Type: ")
        grade = input("Grade: ")

        student.add_test(type,grade)
    elif(action == EditActions.LISTTESTS):
        student.print_tests()