import json
import os
import sys

#ToDos
#   1. Make the user communication as good as you can.

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]["grade_breakdown"]
    return grades

def loadUserGradesData():
    # ToDo: Check if the file exists
    with open('gc_grades.json') as data_file:
        user_data = json.load(data_file)
    return user_data

def askForAssignmentMarks(grades, current_grades):
    if ("mygrades" not in current_grades.keys()) :
        current_grades = {"mygrades": {}}

    for key in grades:
        print("\nPercent for", key, "is", grades[key])
        # ToDo: Handle the case when the file was empty (forst tiem user)
        print("\nYour grade for", key, "is", current_grades["mygrades"][key])
        if (float(current_grades["mygrades"][key]) > -1):
            update = input("Do you want to change? ")
            if (update == "no"):
                continue
        # ToDo: Handle the case when the user types a text instead of a number
        # ToDo: Handle the case when the user types a non-valid number ( >100 or other incorrect numbers)
        current_grades["mygrades"][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
        if current_grades["mygrades"][key] > 100 or current_grades["mygrades"][key] < -1:
            print("the number you entered is invalid. Please input number between -1 and 100")
        else:
            continue
    return current_grades

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades):
    curr_grade = 0
    # ToDo: Handle the case when the file was empty (forst tiem user)
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = int(current_grades["mygrades"][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print ("\nYour GPA is: ", curr_grade)

def main():
    grades_setup = loadSetupData()
    a = os.listdir()
    if 'gc_grades.json' not in a:
        print("file does not exist")
    else:
        user_grades = loadUserGradesData()
        import sys
        file = 'gc_grades.json'
        if os.stat(file).st_size == 0:
            print('file is empty')

        else:
            printCurrentGrade(grades_setup, user_grades)
            current_grades = askForAssignmentMarks(grades_setup, user_grades)
            saveGrades(current_grades)
            printCurrentGrade(grades_setup, current_grades)
            sys.exit()


main()