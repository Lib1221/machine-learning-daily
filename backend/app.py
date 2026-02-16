"""
Cognitive Echo - FastAPI Backend
Day 2: Data Collection Engine
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import os
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI(title="Cognitive Echo API", version="0.1.0")

# Add CORS middleware for Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database configuration
DATABASE_PATH = "cognitive_echo.db"

# Pydantic models
class UserResponse(BaseModel):
    user_id: str
    question_id: int
    answer: str
    reaction_time_ms: int
    confidence_score: int

class UserSummary(BaseModel):
    user_id: str
    total_responses: int
    average_reaction_time: float
    last_response_date: Optional[str]

# Database initialization
def init_database():
    """Initialize SQLite database with required schema."""
    if not os.path.exists(DATABASE_PATH):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE user_responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                question_id INTEGER NOT NULL,
                answer TEXT NOT NULL,
                reaction_time_ms INTEGER NOT NULL,
                confidence_score INTEGER NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE INDEX idx_user_id ON user_responses(user_id)
        """)
        
        conn.commit()
        conn.close()
        print("Database initialized successfully.")

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    init_database()

# Endpoints
@app.post("/submit-response")
async def submit_response(response: UserResponse):
    """
    Submit a user response to a question.
    Records reaction time, answer, and confidence score.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO user_responses 
            (user_id, question_id, answer, reaction_time_ms, confidence_score)
            VALUES (?, ?, ?, ?, ?)
        """, (response.user_id, response.question_id, response.answer, 
              response.reaction_time_ms, response.confidence_score))
        
        conn.commit()
        conn.close()
        
        return {
            "status": "success",
            "message": "Response recorded successfully",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/user-summary/{user_id}")
async def get_user_summary(user_id: str):
    """
    Retrieve a summary of user responses.
    Includes total responses, average reaction time, and last response date.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT COUNT(*), AVG(reaction_time_ms), MAX(timestamp)
            FROM user_responses
            WHERE user_id = ?
        """, (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result[0] == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {
            "user_id": user_id,
            "total_responses": result[0],
            "average_reaction_time": round(result[1], 2),
            "last_response_date": result[2]
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "Cognitive Echo API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
