from enum import Enum
from functions import *
import math

watching = None
students = []

class Test:
    def __init__(self,type,grade) -> None:
        self.type = type
        self.grade = grade

class Human:
    def __init__(self,first_name,last_name,identifier) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.identifier = identifier

    def __str__(self) -> str:
        return f"{self.name} - {self.identifier}"   

    def GetFullName(self):
        return f"{self.first_name} {self.last_name}"     

class Student(Human):
    def __init__(self, first_name, last_name, identifier) -> None:
        super().__init__(first_name, last_name, identifier)
        self.test_list=[]

    def add_test(self,type,grade):
        self.test_list.append(Test(type,grade))

    def print_tests(self):
        average = 0
        for test in self.test_list:
            print(f"Test: {test.type},  Grade: {test.grade}")
            average = average + int(test.grade)
    
        print(f"Average: {math.floor(average / len(self.test_list))}")

class Actions(Enum):
    ADD = 1
    SEARCH = 2  
    LIST = 3
    PRINTALL = 4
    EDIT = 5

def DoWhile():
    global watching
    while True:
        PrintActions(Actions)
        if(watching != None):
            print(f"Watching Student: {watching.GetFullName()}")

        user_action = input("Choose Your Action: ")
        user_action = Actions(int(user_action))

        if(user_action == Actions.ADD):
            AddStudent(students)
        elif(user_action == Actions.SEARCH):
            student = FindStudent(students)
            if(not student or student == None):
                print("Student With This ID Number Wasn't Found!")
                continue
            watching = student
            print(f"Found: {watching.GetFullName()}")

        elif(user_action == Actions.LIST):
            PrintAllStudents(students)
        elif(user_action == Actions.PRINTALL):
            print(students)
        elif(user_action == Actions.EDIT):
            if(watching and watching != None): EditStudent(watching)
            else: print("No Student Found")


if __name__ == "__main__":
    student = Student("Eyal", "Test", "21744353")
    

    students.append(student)
    DoWhile()