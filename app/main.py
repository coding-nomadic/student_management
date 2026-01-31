# app/main.py
from fastapi import FastAPI
from app.api.student_routes import router as student_router
import uvicorn

app = FastAPI(title="School Management API")

# include router
app.include_router(student_router)

# Run Uvicorn locally if this file is executed directly
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)