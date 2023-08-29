from enum import Enum
from functions import *
import math
import time

USEDEFAULTS = False
watching = None
students = []

class Test:
    def __init__(self,identifier,fullname,type,grade) -> None:
        self.identifier = identifier
        self.fullname = fullname
        self.type = type
        self.grade = grade

class Human:
    def __init__(self,first_name,last_name,identifier) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.identifier = identifier

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.identifier}"   

    def GetFullName(self):
        return f"{self.first_name} {self.last_name}"     

class Student(Human):
    def __init__(self, first_name, last_name, identifier) -> None:
        super().__init__(first_name, last_name, identifier)
        self.test_list=[]

    def add_test(self,type,grade):
        self.test_list.append(Test(self.identifier,self.GetFullName(),type,grade))

    def print_tests(self):
        average = 0
        for test in self.test_list:
            print(f"Test: {test.type},  Grade: {test.grade}")
            average = average + int(test.grade)
    
        print(f"Average: {math.floor(average / len(self.test_list))}")

    def get_tests(self):
        AllTests = []
        for test in self.test_list:
            AllTests.append({"identifier" : test.identifier, "fullname": test.fullname, "type": test.type, "grade" : test.grade})

        return AllTests


class Actions(Enum):
    ADD = 1
    REMOVE = 2
    SEARCH = 3  
    PRINTS = 4
    EDIT = 5
    CLOSE = 6

def DoWhile():
    global watching


    while True:
        PrintActions(Actions)
        if watching is not None:
            print(f"Watching Student: {watching.GetFullName()}")

        user_action = GetActionInput(Actions)
       
        if user_action is None:
            continue

        user_action = Actions(int(user_action))

        if(user_action == Actions.ADD):
            AddStudent(students)
        elif(user_action == Actions.REMOVE):
            RemoveStudent(students)
        elif(user_action == Actions.SEARCH):
            
            student = FindStudent(students)

            if(student == "REMOVE"):
                if watching and watching is not None:
                    print(f"Stopped Watching {watching}")
                    watching = None
                    continue

            if not student or student is None:
                print("Student With This ID Number Wasn't Found!")
                continue
            
            watching = student
            print(f"Found: {watching.GetFullName()}")

        elif(user_action == Actions.PRINTS):
            SelectList(students)
        elif(user_action == Actions.EDIT):
            if watching and watching is not None: EditStudent(students,watching)
            else: print("Not Watching A Student Found, Use The Search Function")
        elif(user_action == Actions.CLOSE):
            seconds = 3
            dot = "."
            for x in range(seconds):
                print(f"Closing Program In \033[95m{seconds - x}\033[0m Seconds")
                time.sleep(1)
            return


if __name__ == "__main__":
    students = load_students('students_data.pkl')
    if(not students):
        print("\033[4mNo Students Found In Database\033[0m")
        if(USEDEFAULTS):
            print("Using Default Values")
            student = Student("Eyal", "Avramovhitz", "11")
            student2 = Student("Professor", "Einstein", "22")
            student.add_test("math",50)
            student.add_test("history",74)

            student2.add_test("history",34)
            student2.add_test("math",74)
            

            students.append(student)
            students.append(student2)
    else:
        print(f"\033[92mLoaded {len(students)} Student{'s' if len(students) != 1 else ''} From Database\033[0m")

    DoWhile()
    print("-" * 43)
    print(f"\033[92mSaving {len(students)} Student{'s' if len(students) != 1 else ''} To Database\033[0m")
    save_students(students, 'students_data.pkl')