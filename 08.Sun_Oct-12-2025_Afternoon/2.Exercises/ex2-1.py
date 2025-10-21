import sqlite3

conn = sqlite3.connect('ex2-1.db')
insert_to_doctor = """INSERT INTO doctors (firstName, lastName, joiningDate, salary, address) values (?, ?, ?, ?, ?)"""
cur = conn.cursor()

def selectStatement():
    cur.execute("SELECT * FROM doctors")
    for row in cur.fetchall():
        print(row)

def insertStatement(firstName, lastName, joiningDate, salary, address):
    data = [(f'{firstName}', f'{lastName}', f'{joiningDate}', f'{salary}', f'{address}')]
    cur.executemany(insert_to_doctor, data)
    conn.commit()

def updateStatement(column, value, id):
    cur.execute(f"UPDATE doctors set {column} = {value} where id = {id}")
    conn.commit()

def deleteStatement(id):
    cur.execute(f"DELETE FROM doctors where id = {id}")
    conn.commit()

if conn:
    print('Connect success!')
    # cur.execute("""
    # create table doctors (
    #     id integer primary key autoincrement,
    #     firstName text,
    #     lastName text,
    #     joiningDate date,
    #     salary float,
    #     address text
    # )
    # """)
    print('Select Statement')
    selectStatement()
    print('=================')
    print('Insert Statement')
    # insertStatement('Hoang', 'Nguyen', '20/10', 100, '64')
    # print('=================')
    print('Update Statement')
    updateStatement('firstName', 'Hoang', 2)
    print('=================')
    print('Delete Statement')
    deleteStatement()
    print('=================')
    conn.close()
else:
    print('Connect failed!')