import sqlite3
conn = sqlite3.connect("test_db.db")
insert_to_user = """insert into users (name, email) values (?, ?)"""
if conn:
    cursor = conn.cursor()
    print('Connect success!')
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)
else:
    print('Connect failed!')