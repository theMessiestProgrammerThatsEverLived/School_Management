from modules import *


def userMenu():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print(''' 
CHOOSE USER ACCOUNT:
    1) ADMIN
    2) TEACHER
    3) STUDENT
    4) ABOUT
    5) EXIT''')
    choice = getChoice()
    return choice


def adminMenu():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
CHOOSE OPERATION:
    1) MODIFY EXAM LIST
    2) MODIFY STUDENT LIST
    3) MODIFY TEACHER LIST
    4) MODIFY SUBJECT LIST
    5) MODIFY CLASS LIST
    6) EXIT ''')
    choice = getChoice()
    return choice


def teacherMenu():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
TEACHER MENU:
    1) ATTENDANCE
    2) MARKS
    3) REPORT-CARD
    4) EXIT ''')
    choice = getChoice()
    return choice


def studentMenu():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
STUDENT MENU:
    1) VIEW ATTENDANCE
    2) VIEW MARKSHEET        
    3) EXIT ''')
    choice = getChoice()
    return choice


def adminEXAM():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
-----------EXAM--------------
    1) VIEW EXAM
    2) ADD EXAM
    3) DELETE EXAM
    4) BACKUP
    5) EXIT ''')
    choice = getChoice()
    return choice


def adminSTUDENT():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------STUDENT----------
    1) VIEW STUDENT
    2) ADD STUDENT
    3) DELETE STUDENT
    4) CHANGE DETAILS
    5) BACKUP
    6) EXIT ''')
    choice = getChoice()
    return choice


def adminTEACHER():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------TEACHER----------
    1) VIEW TEACHER
    2) ADD TEACHER
    3) DELETE TEACHER
    4) BACKUP
    5) EXIT ''')
    choice = getChoice()
    return choice


def adminSUBJECT():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------SUBJECT----------    
    1) VIEW SUBJECT
    2) ADD SUBJECT
    3) DELETE SUBJECT
    4) BACKUP
    5) EXIT ''')
    choice = getChoice()
    return choice


def adminCLASS():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
------------CLASS-----------    
    1) VIEW CLASS
    2) ADD CLASS
    3) DELETE CLASS
    4) BACKUP
    5) EXIT ''')
    choice = getChoice()
    return choice


def teacherATTENDANCE():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------ATTENDANCE----------    
    1) VIEW ATTENDANCE
    2) ENTER ATTENDANCE
    3) EXIT ''')
    choice = getChoice()
    return choice


def teacherMARKS():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------MARKS----------    
    1) VIEW MARKS
    2) ENTER MARKS
    3) EXIT ''')
    choice = getChoice()
    return choice


def studentViewFactor():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------VIEW STUDENT----------    
    1) BASED ON ADMISSION NUMBER
    2) BASED ON CLASS ID
    3) VIEW ALL
    4) EXIT ''')
    choice = getChoice()
    return choice


def studentDetailFactor():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
--------CHANGE DETAILS----------
    1) NAME
    2) DATE OF BIRTH 
    3) ADDRESS 
    4) PHONE NUMBER
    5) EXIT ''')
    choice = getChoice()
    return choice


def attendanceViewFactor():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------VIEW ATTENDANCE----------    
    1) BASED ON DATE
    2) BASED ON STUDENT ID
    3) EXIT ''')
    choice = getChoice()
    return choice


def marksViewFactor():
    cls()
    print(
        '==========================================================SCHOOL MANAGEMENT==========================================================')
    print('''
---------VIEW MARKS----------    
    1) BASED ON STUDENT ID
    2) VIEW ALL
    3) EXIT ''')
    choice = getChoice()
    return choice
