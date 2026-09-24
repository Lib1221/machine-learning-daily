# Day 2: Data Collection Engine

## Objective
Build a FastAPI backend to handle user responses, reaction times, and confidence scores. Establish the data pipeline for the Cognitive Echo system.

## Implementation Details

### 1. FastAPI Application (`backend/app.py`)
The backend is structured as a RESTful API with the following features:

**Endpoints:**
- `POST /submit-response`: Records user responses with reaction time and confidence score
- `GET /user-summary/{user_id}`: Retrieves aggregated user statistics
- `GET /health`: Health check endpoint

**Database Integration:**
- SQLite database (`cognitive_echo.db`) for local data storage
- Automatic schema initialization on first run
- Indexed queries on `user_id` for efficient retrieval

### 2. Database Schema
```sql
CREATE TABLE user_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    question_id INTEGER NOT NULL,
    answer TEXT NOT NULL,
    reaction_time_ms INTEGER NOT NULL,
    confidence_score INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Request/Response Models
- **UserResponse**: Captures question responses with reaction time and confidence
- **UserSummary**: Returns aggregated statistics for a user

### 4. CORS Configuration
Enabled CORS middleware to allow requests from Flutter frontend on any origin.

## How to Run

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:8000`

## Testing

### Submit a Response
```bash
curl -X POST "http://localhost:8000/submit-response" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "question_id": 1,
    "answer": "Option A",
    "reaction_time_ms": 1250,
    "confidence_score": 8
  }'
```

### Get User Summary
```bash
curl "http://localhost:8000/user-summary/user123"
```

## Next Steps (Day 3)
- Build Flutter interactive UI
- Implement timer system with millisecond precision
- Connect frontend to backend endpoints

---
*Day 2 completed: Data collection engine is ready for integration.*
