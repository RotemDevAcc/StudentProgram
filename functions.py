import random
from enum import Enum
from app import Student
import math
import pickle

def save_students(students, filename):
    with open(filename, 'wb') as file:
        pickle.dump(students, file)

def load_students(filename):
    try:
        with open(filename, 'rb') as file:
            students = pickle.load(file)
        return students
    except FileNotFoundError:
        return []

def GetActionInput(Actions):
    user_action = input("Choose Your Action: ")
    if(not user_action or user_action == None): 
        return 
    if(not user_action.strip().isdigit()): 
        print("Action Must be A Number")
        return 
        
    user_action = int(user_action)

    if user_action <= 0:
        print("Action Must Not Be 0 Or Below")
        return None

    if user_action > len(Actions): 
        print(f"Action Must not be higher than {len(Actions)}")
        return None
    
    return user_action
     

def AddStudent(students):
    first_name = input("Enter \033[95mFirst Name\033[0m: ")
    if not first_name:
        print("\033[93mFirstname Must Be Specified\033[0m")
        return
    last_name = input("Enter \033[95mLast Name\033[0m: ")

    if not last_name:
        print("\033[93mLastname Must Be Specified\033[0m")
        return
    

    id_number = GetRandomID(students)
    

    student = Student(first_name, last_name, id_number)
    students.append(student)
    save_students(students, 'students_data.pkl')
    print(f"Student \033[92m{student.GetFullName()}\033[0m added with ID: \033[94m{id_number}\033[0m")

def RemoveStudent(students):
    identifier = input("Enter Student Identifier: ")
    if(not identifier or identifier is None):
        print("\033[93midentifier Must Be Specified\033[0m")
        return
    student_to_remove = GetStudentByIdentifier(students,identifier)


    if student_to_remove is not None:
        students.remove(student_to_remove)
        print(f"Student {student_to_remove.GetFullName()} (ID: {identifier}) has been removed.")
        save_students(students, 'students_data.pkl')
    else:
        print(f"No student with ID {identifier} found.")


def GetRandomID(students):
    randomid = random.randint(210000000,450000000)

    while GetStudentByIdentifier(students,str(randomid)):
        randomid = random.randint(210000000,450000000)
        print(f"Student ID {randomid} Already Used")


    return str(randomid)

def FindStudent(students):
    id_number = input("Enter ID Number: ")

    if(id_number == None or not id_number): return None


    if(not id_number.strip().isdigit()): return None

    for student in students:
        if(student.identifier == id_number):
            return student
        
    return None

def GetStudentByIdentifier(students,identifier):
    for student in students:
        if(student.identifier == identifier):
            return student
        

    return None

def calculate_average_grade(student):
    if not student.test_list:
        return 0  # Handle the case where there are no tests
    total_grade = sum(test.grade for test in student.test_list)
    return total_grade / len(student.test_list)

def PrintAllStudentsByGrades(students,lowergrade):
    # Create a list of tuples with each student's identifier and their average grade
    students_with_avg_grades = [(student.identifier, calculate_average_grade(student)) for student in students]

    # Sort the list of students by average grade (in descending order)
    students_with_avg_grades.sort(key=lambda x: x[1], reverse=not lowergrade)

    for student_identifier, _ in students_with_avg_grades:
        # Find the student with the matching identifier
        student = next(student for student in students if student.identifier == student_identifier)

        # Print test details for the student
        print(f"\033[95mStudent: {student.GetFullName()} (ID: {student.identifier})\033[0m")
        average = 0
        for test in student.get_tests():
            average = average + int(test['grade'])
            print(f"  Type: {test['type']}, Grade: {test['grade']:.2f}")
    
        print(f"  \033[92mAverage Score: {math.floor(average / len(student.get_tests())):.2f}\033[0m")

def FindTheGreatestStudent(students,worst):
    # Create a list of tuples with each student's identifier and their average grade

    students_with_avg_grades = [(student.identifier, calculate_average_grade(student)) for student in students]

    # Sort the list of students by average grade (in descending order)
    students_with_avg_grades.sort(key=lambda x: x[1], reverse=not worst)

    for student_identifier, _ in students_with_avg_grades:
        # Find the student with the matching identifier
        thestudent = GetStudentByIdentifier(students,student_identifier)
        return thestudent,calculate_average_grade(thestudent)
    

    return None,None

    


class ListActions(Enum):
    BGRADE = 1
    LGRADE = 2
    BEST = 3
    WORST = 4
    ALL = 5



def SelectList(students):

    if len(students) == 0:
        print("\033[91mNo Students Are Available\033[0m")
        return

    print("\033[94mHow Do You Want To List The Students?\033[0m")
    for action in ListActions:
        print(f"{action.name} - {action.value}")

    action = ListActions(int(input(f"Choose Your Action: ")))

    if(action == ListActions.BGRADE):
        PrintAllStudentsByGrades(students,False)
    elif(action == ListActions.LGRADE):
        PrintAllStudentsByGrades(students,True)
    elif(action == ListActions.BEST):
        best,score = FindTheGreatestStudent(students,False)
        print(f"\033[92mThe Best Student Is: {best} With An Average Score Of: {score}\033[0m")
    elif(action == ListActions.WORST):
        worst,score = FindTheGreatestStudent(students,True)
        print(f"\033[91mThe Worst Student Is: {worst} With An Average Score Of: {score}\033[0m")
    elif(action == ListActions.ALL):
        print("-" * 43)
        print("List of Students:")
        print("-" * 43)

        for student in students:
            print(f"Name: {student.GetFullName()}")
            print(f"ID: {student.identifier}")
            print("Tests:")
            for test in student.get_tests():
                print(f"  Type: {test['type']}, Grade: {test['grade']:.2f}")
                
            print(f"\033[92mAverage Score: {'No tests' if calculate_average_grade(student) == 0 else calculate_average_grade(student)}\033[0m")
            print("-" * 43)  # Separator between students


    
       

def PrintAllStudents(students):
    for student in students:
        print(type(student))

def PrintActions(actions):
    for action in actions:
        print(f"{action.name} - {action.value}")

class EditActions(Enum):
    ADDTEST = 1
    LISTTESTS = 2

def EditStudent(students,student):
    for action in EditActions:
        print(f"{action.name} - {action.value}")

    action = EditActions(int(input(f"Choose Your Action For {student.GetFullName()}: ")))

    if(action == EditActions.ADDTEST):
        type = input("Test Type (math,history...): ")
        if not type:
            print("\033[93mType Must Be Specified\033[0m")
            return
        grade = input("Grade (0 ~ 100): ")

        if(not grade):
            print("\033[93mGrade Must Be Specified\033[0m")
            return
        
        if not grade.strip().isdigit():
            print("\033[93mGrade Must Be A Number\033[0m")
            return
        
        grade = int(grade)

        student.add_test(type,grade)
        save_students(students, 'students_data.pkl')
    elif(action == EditActions.LISTTESTS):
        student.print_tests()