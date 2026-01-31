import psycopg2

# PostgreSQL connection parameters
DB_HOST = "localhost"
DB_NAME = "test"
DB_USER = "postgres"
DB_PASSWORD = "test"
DB_PORT = "5432"

# SQL to create tables
create_tables_sql = """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    enrollment_year INT
);

CREATE TABLE IF NOT EXISTS courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits > 0)
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    semester VARCHAR(20),
    year INT
);

CREATE TABLE IF NOT EXISTS grades (
    grade_id SERIAL PRIMARY KEY,
    enrollment_id INT REFERENCES enrollments(enrollment_id),
    grade DECIMAL(4,2) CHECK (grade BETWEEN 0 AND 4)
);
"""

# SQL to insert initial data
insert_data_sql = """
INSERT INTO students (name, email, enrollment_year) VALUES
('Tenzin', 'tenzin@mail.com', 2023),
('Maya', 'maya@mail.com', 2022),
('John', 'john@mail.com', 2023);

INSERT INTO courses (course_name, credits) VALUES
('Databases', 3),
('Algorithms', 4),
('Operating Systems', 3);

INSERT INTO enrollments (student_id, course_id, semester, year) VALUES
(1, 1, 'Fall', 2024),
(1, 2, 'Fall', 2024),
(2, 1, 'Spring', 2024),
(3, 3, 'Fall', 2024);

INSERT INTO grades (enrollment_id, grade) VALUES
(1, 3.8),
(2, 3.6),
(3, 3.9),
(4, 3.2);
"""

def setup_database():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()
        # Create tables
        cursor.execute(create_tables_sql)
        # Insert data
        cursor.execute(insert_data_sql)
        conn.commit()
        print("Tables created and data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
