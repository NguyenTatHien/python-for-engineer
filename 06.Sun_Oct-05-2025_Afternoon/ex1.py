import sqlite3
conn = sqlite3.connect("people.db")
insert_to_user = """insert into users (name, email) values (?, ?)"""
if conn:
    cursor = conn.cursor()
    print('Connect success!')
    # cursor.execute("""
    # CREATE TABLE users (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT,
    #     email TEXT
    # )
    # """)
    # print("Create table user successful!")

    # data = [('hien', 'tathien2003@gmail.com'), ('hi', 'tathienbadao@gmail.com'), ('hoho', 'hoho@gmail.com')]
    # cursor.executemany(insert_to_user, data)

    # cursor.execute("""delete from users where email='hoho@gmail.com'""")
    # print('delete successful!')

    cursor.execute("""select * from users order by email asc""")
    for row in cursor.fetchall():
        print(row)
    conn.commit()
    conn.close()
else:
    print('Connect failed!')