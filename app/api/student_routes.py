# app/api/student_routes.py
from fastapi import APIRouter, HTTPException
from app.schemas.student_schema import StudentResponse, StudentRequest
from app.crud.student_crud import (
    create_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter()

# Create a new student
@router.post("/student", response_model=StudentResponse)
def add_student(student: StudentRequest):
    return create_student(student)

# Get all students
@router.get("/students", response_model=list[StudentResponse])
def read_students():
    return get_students()

# Get a student by ID
@router.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int):
    student = get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update a student by ID
@router.put("/students/{student_id}", response_model=StudentResponse)
def edit_student(student_id: int, student: StudentRequest):
    updated = update_student(student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

# Delete a student by ID
@router.delete("/students/{student_id}")
def remove_student(student_id: int):
    success = delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}
