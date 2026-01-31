from pydantic import BaseModel, Field, EmailStr, conint

class StudentRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)  # Required, 2-100 chars
    email: EmailStr  # Valid email format
    enrollment_year: conint(ge=1900, le=2100)

class StudentResponse(StudentRequest):
    student_id: int