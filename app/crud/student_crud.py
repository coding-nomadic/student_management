# app/crud/student_crud.py
from app.db.connection import get_connection

def create_student(student):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, email, enrollment_year) VALUES (%s, %s, %s) RETURNING student_id;",
        (student.name, student.email, student.enrollment_year)
    )
    student_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"student_id": student_id, "name": student.name, "email": student.email, "enrollment_year": student.enrollment_year}

def get_student_by_id(student_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT student_id, name, email, enrollment_year FROM students WHERE student_id = %s;",
        (student_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {"student_id": row[0], "name": row[1], "email": row[2], "enrollment_year": row[3]}
    return None

def update_student(student_id: int, student):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET name = %s, email = %s, enrollment_year = %s WHERE student_id = %s RETURNING student_id;",
        (student.name, student.email, student.enrollment_year, student_id)
    )
    updated_id = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if updated_id:
        return {"student_id": student_id, "name": student.name, "email": student.email, "enrollment_year": student.enrollment_year}
    return None

def delete_student(student_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM students WHERE student_id = %s RETURNING student_id;",
        (student_id,)
    )
    deleted_id = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return bool(deleted_id)


def get_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT student_id, name, email, enrollment_year FROM students;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"student_id": r[0], "name": r[1], "email": r[2], "enrollment_year": r[3]} for r in rows]
