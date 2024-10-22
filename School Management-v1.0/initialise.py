from MAIN.modules import *


choice = input('IF DATABASE NAME CONFLICT OCCURS, THE EXISTING DATABASE WILL BE OVERWRITTEN(Y/N): ').lower() == 'y'
host, user, password = getCredentials()
db, cur = mySql(host, user, password, database=False)

if choice and db.is_connected():

    try:
        if checkDatabase(cur):
            cur.execute('drop database school;')

        with open('SQL\\databaseCreationCommands.txt') as file:
            data = file.read().split('-----')

            for quires in data:
            
                cur.execute(quires.strip())

        print('ASSIGN ADMIN')
        adminName = input('NAME: ')
        adminPassword = input('PASSWORD: ')
        print('CREATE CLASS')
        classId =int(input("CREATE ADMIN CLASS ID: "))
        grade = str(input('GRADE: '))
        section = str(input('SECTION: '))
        cur.execute(f"insert into class values('{grade}', '{section}', {classId})")
        cur.execute(f"""insert into teacher values('{adminName}','T',101, {classId},'{adminPassword}')""")
        db.commit()

    except Exception as e:
        print(str(e) + "\nTRY RE-ENTERING THE VALUE CORRECTLY")
        wait()
    


else:
    if not db.is_connected():
        print("CANNOT CONNECT TO MY-SQL")
    else:
        print("SOMETHING WENT WRONG")
