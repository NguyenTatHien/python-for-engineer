import sqlite3
conn = sqlite3.connect('doctors.db')

def select_statement():
    cursor.execute("SELECT * FROM doctors")
    for row in cursor.fetchall():
        print(row)
    conn.commit()

def insert_statement(firstName, lastName, joinDate, salary, address):
    insert_query = "INSERT INTO doctors (firstName, lastName, joiningDate, salary, address) values (?, ?, ?, ?, ?)"
    data = [(firstName, lastName, joinDate, salary, address)]
    cursor.executemany(insert_query, data)
    conn.commit()

def update_statement(id, column, value):
    cursor.execute(f"UPDATE doctors set {column} = ? where id = ?", (value, id))
    conn.commit()

def delete_statement(id):
    cursor.execute(f"DELETE FROM doctors where id = {id}")
    conn.commit()

if conn:
    cursor = conn.cursor()
    print('Connect success!')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT,
        lastName TEXT,
        joiningDate TEXT,
        salary NUMERIC,
        address TEXT
    )
    """)
    insert_statement('Hoang', 'Nguyen', '17/10/2025', 100, 'HU')
    print('select statement')
    select_statement()
    ##############
    print('insert statement')
    insert_statement('Hien', 'Nguyen', '20/10/2025', 200, 'SO')
    select_statement()
    ##############
    print('update statement')
    update_statement(1, 'firstName', 'Harry')
    select_statement()
    ##############
    print('delete statement')
    delete_statement(1)
    select_statement()
    conn.close()

else:
    print('Connect failed!')

