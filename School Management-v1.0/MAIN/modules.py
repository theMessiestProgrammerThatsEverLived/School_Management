from mysql.connector import *
from os import system
from getpass import getpass
from csv import reader, writer


def cls():
    system('cls')


def wait():
    input("PRESS ANY KEY TO CONTINUE: ")


def getChoice():
    choice = int(input('ENTER OPTION: '))
    cls()
    return choice


def getPassword(value='Password'):
    password = getpass(f"{value}: ")
    return password


def executeAndFetch(query, cur):
    cur.execute(query)
    data = cur.fetchall()

    return data


def mySql(host, user, password, database=True):
    if database:
        db = connect(host=host, user=user, password=password, database='school')
        cur = db.cursor()

    else:
        db = connect(host=host, user=user, password=password)
        cur = db.cursor()

    return db, cur


def checkDatabase(cur):
    data = executeAndFetch('show databases;', cur)
    for line in data:

        if str(line[0]).lower() == 'school':
            return True

        else:
            continue

    return False


def showRec(data):
    length = int()
    stRec = str()

    for rec in data:
        record = list()

        for element in rec:
            record.append(element)

            if len(str(element)) > length:
                length = len(str(element))

    for rec in data:
        stRec += '| '

        for element in rec:

            if len(str(element)) == length:
                stRec += f'{element} | '

            else:
                fills = length - len(str(element))
                gap = ' ' * fills
                stRec += f"{element}{gap} | "

        stRec += '\n'

    return stRec


def getValue(columnName, table, args, cur):
    cur.execute('use school;')
    cur.execute(f'select {columnName} from {table} where {args};')
    return cur.fetchall()


def getColumn(data, index=0):
    end = tuple()
    for i in data:
        end += (i[index],)
    return end


def header(tableName, cur):
    data = executeAndFetch(f"desc {tableName};", cur)
    data = [getColumn(data, 0)]
    return data


def assignUniqueId(table, columnName, cur):
    data = executeAndFetch(f'select {columnName} from {table};', cur)
    uId = int()
    while (uId,) in data:
        uId += 1
    return uId


def backup(data, text='BACKUP'):
    try:
        filePath = str(input(f'Enter {text} FILE PATH: '))
        fileName = str(input(f'Enter {text} FILE NAME: '))

        with open(f'{filePath}\\{fileName}.txt', 'w') as file:
            file.write(data)

        return data

    except Exception as e:
        return str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY"


def generateReportCard(admissionNumber, examId, cur):
    data = executeAndFetch(f"""
    SELECT st.Name as student_name, st.admissionNumber, 
    ex.examName, ex.dateOfExam,
    sub.subjectName, ms.marks, ms.result
    FROM mark_sheet ms
    JOIN student st ON ms.admissionNumber = st.admissionNumber
    JOIN exam ex ON ms.examId = ex.examId
    JOIN subject sub ON ms.subjectId = sub.subjectId
    WHERE ms.admissionNumber = {admissionNumber} AND ms.examId = {examId}
    """, cur)
    headerList = [('NAME', 'ADMISSION NUMBER', 'EXAM NAME', 'DATE OF EXAM', 'SUBJECT NAME', 'MARKS', 'RESULT')]
    print(backup(showRec(headerList + data)))
    return '.................GENERATED....................'


def checkUser(id, type, cur):
    if type.lower() == 'teacher':
        data = getValue('teacherId', 'teacher', f' teacherId = {id}', cur)
        if data == list():
            return False
        
        else:
            return True
    
    elif type.lower() == 'student':
        data = getValue('admissionNumber', 'student', f' admissionNumber = {id}', cur)
        
        if data == list():
            return False
        
        else:
            return True


def writeCredentials(credentialList):
    with open('docs\\credentials.csv', 'w', newline='') as file:
        cw = writer(file, delimiter=',')
        cw.writerows([['hostName', 'userName', 'Password'], credentialList])

    return credentialList


def getCredentials():
    with open('docs\\credentials.csv') as file:
        cr = reader(file, delimiter=',')
        rowcount = 0
        for rows in cr:
            if rowcount == 1:
                return rows

            else:
                rowcount += 1

