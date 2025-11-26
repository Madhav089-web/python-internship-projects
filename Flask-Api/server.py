from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
db = "employees.db"


def connection(db):

    return sqlite3.connect(db)


con = connection(db)



cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    salary REAL
)
""")
con.commit()


@app.get("/")
def home():
    return {"message": "Hello From Python 🐉!"}


@app.post("/employees")
def add_employee():
    data = request.json



    cur.execute("INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)",
                

                (data["name"], data["role"], data["salary"]))
    con.commit()
    return {"message": "Employee added successfully"}, 201


@app.get("/employees")
def get_employees():
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    people = []
    for r in rows:
        people.append({"id": r[0], "name": r[1], "role": r[2], "salary": r[3]})
    return jsonify(people)


@app.get("/employees/<int:id>")
def get_employee(id):
    cur.execute("SELECT * FROM employees WHERE id = ?", (id,))
    r = cur.fetchone()
    if r:
        return {"id": r[0], "name": r[1], "role": r[2], "salary": r[3]}
    return {"error": "Employee not found"}, 404


@app.put("/employees/<int:id>")
def update_employee(id):
    data = request.json
    cur.execute("UPDATE employees SET name = ?, role = ?, salary = ? WHERE id = ?",
                (data["name"], data["role"], data["salary"], id))
    con.commit()
    return {"message": "Employee updated"}


@app.delete("/employees/<int:id>")
def delete_employee(id):
    cur.execute("DELETE FROM employees WHERE id = ?", (id,))
    con.commit()
    return {"message": "Employee removed"}

app.run()