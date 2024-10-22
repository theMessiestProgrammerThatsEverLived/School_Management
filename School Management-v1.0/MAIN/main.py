from frontEnd import *
from modules import *
from datetime import datetime

host, user, password = getCredentials()
db, cur = mySql(host, user, password)
loop = True

while loop:
    user = userMenu()
    brk = True
    count = int()
    while user == 1 and brk and count <= 3:
        password = getPassword()

        while password == executeAndFetch("select password from teacher where ifAdmin = 'T'", cur)[0][0]:
            choice = adminMenu()

            while choice == 1:
                headerList = header('exam', cur)
                exam = adminEXAM()

                if exam == 1:
                    cls()
                    print(showRec(headerList + executeAndFetch('select * from exam', cur)))
                    wait()

                while exam == 2:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from exam', cur)))
                        examId = assignUniqueId('exam', 'examId', cur)
                        examName = str(input('EXAM NAME: '))
                        if examName == '':
                            break
                        examDate = str(input('EXAM DATE(YYYY-MM-DD): '))
                        cur.execute(f"insert into exam values({examId}, '{examName}', '{examDate}');")
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                while exam == 3:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from exam', cur)))
                        examName = str(input('NAME OF EXAM TO BE REMOVED: '))
                        if examName == '':
                            break
                        cur.execute(f'delete from exam where examName = "{examName}"; ')
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO DELETE MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if exam == 4:
                    cls()
                    data = showRec(headerList + executeAndFetch('select * from exam', cur))
                    print(backup(data))
                    wait()

                if exam == 5:
                    break

            while choice == 2:
                try:
                    headerList = header('student', cur)
                    adminStudent = int(adminSTUDENT())

                    while adminStudent == 1:
                        viewFactor = int(studentViewFactor())

                        if viewFactor == 1:
                            try:
                                cls()
                                admissionNumber = int(input('ENTER THE ADMISSION NUMBER TO BE VIEWED: '))
                                data = headerList + executeAndFetch(
                                    f'''select * from student where admissionNumber={admissionNumber}''', cur)
                                print(showRec(data))
                                wait()

                            except Exception as e:
                                print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                                wait()

                        elif viewFactor == 2:
                            try:
                                cls()
                                classId = int(input('ENTER THE CLASS ID TO BE VIEWED: '))
                                data = headerList + executeAndFetch(
                                    f"""
    select s.admissionNumber, s.Name, s.DOB, s.DOJ, s.address, s.phoneNumber_1, s.phoneNumber_2 from student s 
    join struc_class c on s.admissionNumber = c.admissionNumber
    where c.classID = {classId};""", cur)
                                print(showRec(data))
                                wait()

                            except Exception as e:
                                print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                                wait()

                        elif viewFactor == 3:
                            data = headerList + executeAndFetch('select * from student', cur)
                            print(showRec(data))
                            wait()

                        elif viewFactor == 4:
                            break

                    while adminStudent == 2:
                        try:
                            cls()
                            studentId = assignUniqueId('student', 'admissionNumber', cur)
                            studentName = str(input("ENTER STUDENT NAME: "))
                            if studentName == '':
                                break

                            studentDOB = str(input("ENTER STUDENT DATE OF BIRTH(YYYY-MM-DD): "))
                            studentDOJ = str(datetime.today()).split()[0]
                            studentAddress = str(input("ENTER ADDRESS: "))
                            studentPhNo1 = str(input("ENTER PHONE NUMBER: "))
                            studentPhNo2 = str(input("ENTER ALTERNATE PHONE NUMBER: "))
                            classId = int(input("ENTER ASSIGNED CLASS ID: "))
                            wait()
                            cur.execute(
                                f"insert into student values({studentId}, '{studentName}', '{studentDOB}', '{studentDOJ}', '{studentAddress}', '{studentPhNo1}', '{studentPhNo2}')")
                            cur.execute(f"insert into struc_class values({studentId}, {classId})")
                            db.commit()
                            continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                            if continueOrNot:
                                continue

                            else:
                                break

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()

                    while adminStudent == 3:
                        try:
                            cls()
                            admissionNumber = input('ENTER THE ADMISSION NUMBER TO BE REMOVED: ')

                            if admissionNumber == '':
                                break

                            else:
                                admissionNumber = int(admissionNumber)

                            data = headerList + executeAndFetch(
                                f'select * from student where admissionNumber={admissionNumber}',
                                cur)
                            print(showRec(data))
                            print('RECORD TO BE REMOVED')
                            wait()
                            cur.execute(f'delete from student where admissionNumber={admissionNumber}')
                            db.commit()
                            continueOrNot = input('DO YOU WANT TO DELETE MORE(Y/N): ').lower() == 'y'

                            if continueOrNot:
                                continue

                            else:
                                break

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()

                    while adminStudent == 4:
                        try:
                            cls()
                            admissionNumber = input("ENTER ADMISSION NUMBER OF STUDENT: ")
                            if admissionNumber == '':
                                break

                            else:
                                admissionNumber = int(admissionNumber)

                            change = int(studentDetailFactor())
                            data = headerList + executeAndFetch(
                                f'select * from student where admissionNumber={admissionNumber}', cur)
                            print(showRec(data))

                            if change == 1:
                                studentName = str(input("ENTER STUDENT NAME: "))
                                cur.execute(
                                    f"update student set name = '{studentName}' where admissionNumber = {admissionNumber};")
                                db.commit()

                            elif change == 2:
                                studentDOB = str(input("ENTER STUDENT DATE DO BIRTH(YYYY-MM-DD): "))
                                cur.execute(
                                    f"update student set dob = '{studentDOB}' where admissionNumber = {admissionNumber};")
                                db.commit()

                            elif change == 3:
                                studentAddress = str(input("ENTER ADDRESS: "))
                                cur.execute(
                                    f"update student set address = '{studentAddress}' where admissionNumber = {admissionNumber};")
                                db.commit()

                            elif change == 4:
                                studentPhNo = str(input("ENTER PHONE NUMBER: "))
                                cur.execute(
                                    f"update student set address = '{studentPhNo}' where admissionNumber = {admissionNumber};")
                                db.commit()

                            elif change == 5:
                                break

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()

                    if adminStudent == 5:
                        cls()
                        data = showRec(headerList + executeAndFetch('select * from student', cur))
                        print(backup(data))
                        wait()

                    elif adminStudent == 6:
                        break

                except ValueError:
                    continue

            while choice == 3:
                headerList = header('teacher', cur)
                teacher = adminTEACHER()

                if teacher == 1:
                    cls()
                    print(showRec(headerList + executeAndFetch('select * from teacher', cur)))
                    wait()

                while teacher == 2:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from teacher', cur)))
                        teacherId = assignUniqueId('teacher', 'teacherId', cur)
                        teacherName = input('TEACHER NAME: ')

                        if teacherName == '':
                            break

                        classId = int(input('ASSIGN CLASS: '))
                        teacherPassword = input('TEACHER PASSWORD: ')
                        cur.execute(
                            f"insert into teacher values('{teacherName}', 'F', {teacherId}, {classId}, '{teacherPassword}');")
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                while teacher == 3:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from teacher', cur)))
                        teacherId = str(input('ID OF TEACHER TO BE REMOVED: '))
                        if teacherId == '':
                            break
                        cur.execute(f'delete from teacher where teacherId = {teacherId}; ')
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO DELETE MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if teacher == 4:
                    cls()
                    data = showRec(headerList + executeAndFetch('select * from teacher', cur))
                    print(backup(data))
                    wait()

                if teacher == 5:
                    break

            while choice == 4:
                headerList = header('subject', cur)
                subject = adminSUBJECT()

                if subject == 1:
                    cls()
                    print(showRec(headerList + executeAndFetch('select * from subject', cur)))
                    wait()

                while subject == 2:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from subject', cur)))
                        subjectId = assignUniqueId('subject', 'subjectId', cur)
                        subjectName = input('SUBJECT NAME: ')

                        if subjectName == '':
                            break

                        cur.execute(f"insert into subject values({subjectId}, '{subjectName}');")
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                while subject == 3:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from subject', cur)))
                        subjectId = input('ID OF SUBJECT TO BE REMOVED: ')
                        if subjectId == '':
                            break

                        else:
                            subjectId = int(subjectId)

                        cur.execute(f'delete from subject where subjectId = {subjectId}; ')
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO DELETE MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if subject == 4:
                    cls()
                    data = showRec(headerList + executeAndFetch('select * from subject', cur))
                    print(backup(data))
                    wait()

                if subject == 5:
                    break

            while choice == 5:
                headerList = header('class', cur)
                Class = adminCLASS()

                if Class == 1:
                    cls()
                    print(showRec(headerList + executeAndFetch('select * from class', cur)))
                    wait()

                while Class == 2:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from class', cur)))
                        classId = assignUniqueId('Class', 'ClassId', cur)
                        className = input('ENTER CLASS: ')
                        if className == '':
                            break

                        section = input('ENTER SECTION: ')
                        cur.execute(f"insert into Class values('{className}', '{section}', {classId});")
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                while Class == 3:
                    try:
                        cls()
                        print(showRec(headerList + executeAndFetch('select * from Class', cur)))
                        classId = input('ID OF CLASS TO BE REMOVED: ')
                        if classId == '':
                            break
                        else:
                            classId = int(classId)

                        cur.execute(f'delete from class where classID = {classId}; ')
                        db.commit()
                        continueOrNot = input('DO YOU WANT TO DELETE MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if Class == 4:
                    cls()
                    data = showRec(headerList + executeAndFetch('select * from class', cur))
                    print(backup(data))
                    wait()

                if Class == 5:
                    break

            if choice == 6:
                brk = False
                break

        else:
            count += 1
            print('WRONG PASSWORD :[')
            wait()

    while user == 2 and brk and count <= 3:
        teacherId = int(input('ENTER TEACHER ID: '))
        
        if not checkUser(teacherId, 'teacher', cur):
               print('INCORRECT USERNAME PLEASE RE-ENTER :[')
               wait()
               break
         
        password = getPassword()
        while password == executeAndFetch(f"select password from teacher where teacherId = {teacherId}", cur)[0][0]:
            choice = teacherMenu()

            while choice == 1:
                cls()
                teacherAttendance = teacherATTENDANCE()

                while teacherAttendance == 1:
                    try:
                        cls()
                        classId = int(input('class id: '))
                        viewFactor = attendanceViewFactor()
                        if viewFactor == 1:
                            try:
                                cls()
                                date = str(input("ENTER DATE(YYYY-MM-DD): "))
                                data = executeAndFetch(f"""
select s.name, a.status from struc_class sc 
join attendance a on sc.admissionNumber = a.admissionNumber
join student s on sc.admissionNumber = s.admissionNumber
where sc.classId = {classId} and a.date = "{date}";""", cur)
                                headerList = [('name', 'status')]
                                print(str(showRec(headerList + data)))
                                wait()

                            except Exception as e:
                                print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                                wait()

                        elif viewFactor == 2:
                            try:
                                cls()
                                headerList = header('attendance', cur)
                                admissionNumber = int(input("ENTER ADMISSION NUMBER OF STUDENT: "))
                                requiredMonth = str(input("ENTER THE MONTH NUMBER(01-12): "))
                                data = executeAndFetch(f"""
select * from attendance 
where date like '%-{requiredMonth}-%' and admissionNumber = {admissionNumber}""", cur)
                                print(showRec(headerList + data))
                                wait()

                            except Exception as e:
                                print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                                wait()

                        elif viewFactor == 3:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                while teacherAttendance == 2:
                    try:
                        cls()
                        date = str(datetime.today()).split()[0]
                        admissionNumber = int(input("ENTER ADMISSION NUMBER OF STUDENT: "))
                        status = str(input("ENTER PRESENT(P)\\ ABSENT(A)\\ HALF-DAY(H)\\ ON-DUTY(D): "))
                        cur.execute(f"insert into attendance values({admissionNumber}, '{date}', '{status}')")
                        continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                        if continueOrNot:
                            continue

                        else:
                            break

                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if teacherAttendance == 3:
                    break

            while choice == 2:
                cls()
                teacherMarks = teacherMARKS()

                while teacherMarks == 1:
                    cls()
                    viewFactor = marksViewFactor()

                    if viewFactor == 1:
                        try:
                            cls()
                            admissionNumber = int(input("ENTER ADMISSION NUMBER OF STUDENT: "))
                            exam = str(input("ENTER EXAM NAME: "))
                            data = executeAndFetch(f"""
select s.subjectName, m.marks, m.result from exam e 
join mark_Sheet m on e.examId = m.examId 
join subject s on s.subjectId = m.subjectId 
where m.admissionNumber = {admissionNumber} and e.examName = '{exam}';""", cur)
                            header = [('SUBJECT', 'MARKS', 'RESULT')]
                            print(showRec(header + data))
                            wait()

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()

                    elif viewFactor == 2:
                        try:
                            data = executeAndFetch(f"""
select st.Name, e.examName, s.subjectName, m.marks, m.result from exam e 
join mark_Sheet m on e.examId = m.examId 
join subject s on s.subjectId = m.subjectId
join student st on st.admissionNumber = m.admissionNumber;""", cur)
                            headerList = [('NAME', 'EXAM', 'SUBJECT', 'MARKS', 'RESULT')]
                            print(showRec(headerList + data))
                            wait()

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()

                    elif viewFactor == 3:
                        break

                while teacherMarks == 2:
                    try:
                        examId = int(input("ENTER EXAM ID: "))
                        admissionNumber = int(input("ENTER ADMISSION NUMBER OF STUDENT: "))
                        try:
                            subjectId = str(input("ENTER SUBJECT ID: "))
                            marks = str(input("ENTER MARKS: "))
                            result = str(input("ENTER RESULT: "))
                            cur.execute(
                                f"insert into mark_sheet values({admissionNumber}, {examId}, {subjectId}, {marks},'{result}')")
                            continueOrNot = input('DO YOU WANT TO ADD MORE(Y/N): ').lower() == 'y'

                            if continueOrNot:
                                continue

                            else:
                                Continue = False
                                break

                        except Exception as e:
                            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                            wait()


                    except Exception as e:
                        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                        wait()

                if teacherMarks == 3:
                    break

            if choice == 3:
                cls()
                admissionNumber = int(input('ENTER ADMISSION NUMBER: '))
                examId = int(input('ENTER EXAM ID: '))
                print(generateReportCard(admissionNumber, examId, cur))
                wait()

            elif choice == 4:
                brk = False
                break

        else:
            count += 1
            print('WRONG PASSWORD :[')
            wait()

    while user == 3:
        try:
            cls()
            admissionNumber = int(input('ENTER ADMISSION NUMBER: '))
            
            if not checkUser(admissionNumber, 'student', cur):
               print('INCORRECT USERNAME PLEASE RE-ENTER :[')
               wait()
               break
            
            
            choice = studentMenu()

            if choice == 1:
                try:
                    cls()
                    headerList = header('attendance', cur)
                    requiredMonth = str(input("ENTER THE MONTH NUMBER(01-12): "))
                    data = executeAndFetch(f"""
select * from attendance 
where date like '%-{requiredMonth}-%' and admissionNumber = {admissionNumber}""", cur)
                    print(showRec(headerList + data))
                    wait()
                    

                except Exception as e:
                    print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                    wait()


            elif choice == 2:
                try:
                    cls()
                    requiredExamId = int(input('ENTER THE EXAM ID: '))
                    data = executeAndFetch(f"""
SELECT st.Name as student_name, st.admissionNumber, 
ex.examName, ex.dateOfExam,
sub.subjectName, ms.marks, ms.result
FROM mark_sheet ms
JOIN student st ON ms.admissionNumber = st.admissionNumber
JOIN exam ex ON ms.examId = ex.examId
JOIN subject sub ON ms.subjectId = sub.subjectId
WHERE ms.admissionNumber = {admissionNumber} AND ms.examId = {requiredExamId}
                    """, cur)
                    headerList = [('NAME', 'ADMISSION NUMBER', 'EXAM NAME', 'DATE OF EXAM', 'SUBJECT NAME', 'MARKS', 'RESULT')]
                    print(showRec(headerList + data))
                    wait()

                except Exception as e:
                    print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
                    wait()


            elif choice == 3:
                break

        except Exception as e:
            print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
            wait()

    if user == 4:
        cls()
        print(
        '==================================================ABOUT SCHOOL MANAGEMENT==========================================================')
        with open('docs\\about.txt') as file:
            print(file.read())
        
        wait()
    
    elif user == 5:
        break
