from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Enterprise Student & AI Training Portal",
    description="Production backend gateway for managing student databases and tracking LLM pipelines.",
    version="2.0.0"
)

# Data Schemas for Student Management & AI Metrics
class StudentRecord(BaseModel):
    id: int
    name: str
    course: str
    status: str  # e.g., "Active", "Completed"

class TrainingPipeline(BaseModel):
    model_name: str
    epoch: int
    loss: float
    accuracy: float
    status: str # e.g., "Training", "Deployed"

# Mock Database
students_db = [
    {"id": 1, "name": "Mahnoor Fatima", "course": "Generative AI Training", "status": "Active"}
]

pipelines_db = [
    {"model_name": "Agentic-LLM-v1", "epoch": 50, "loss": 0.024, "accuracy": 98.6, "status": "Deployed"}
]

@app.get("/api/v1/students", tags=["Student Management"])
async def get_all_students():
    return {"status": "success", "data": students_db}

@app.get("/api/v1/ai-pipelines", tags=["AI Pipeline Tracking"])
async def get_pipeline_metrics():
    return {"status": "success", "data": pipelines_db}

@app.get("/health", tags=["System Health"])
async def system_health():
    return {"status": "healthy", "layer": "FastAPI Python Microservice"}
