from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect("doctors.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT,
            lastName TEXT,
            joiningDate TEXT,
            salary NUMERIC,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

# Input data page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fn = request.form['first_name']
        ln = request.form['last_name']
        jd = request.form['joining_date']
        sal = float(request.form['salary'])
        addr = request.form['address']

        conn = sqlite3.connect("doctors.db")
        c = conn.cursor()
        c.execute("INSERT INTO doctors (firstName, lastName, joiningDate, salary, address) VALUES (?, ?, ?, ?, ?)",
                  (fn, ln, jd, sal, addr))
        conn.commit()
        conn.close()

        return render_template('success.html')

    return render_template('form.html')

# View list page
@app.route('/doctors')
def doctors():
    conn = sqlite3.connect("doctors.db")
    c = conn.cursor()
    c.execute("SELECT * FROM doctors")
    rows = c.fetchall()
    conn.close()
    return render_template('list.html', rows=rows)

if __name__ == '__main__':
    create_table()
    app.run()
