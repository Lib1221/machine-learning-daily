# Cognitive Echo: AI Personality & Behavior Analyzer

## Project Overview
Cognitive Echo is an end-to-end intelligent system designed to analyze user personality and behavior through interactive micro-tasks, reaction time analysis, and NLP.

## Day 1: System Design & Definition

### 1. Personality Outputs (The Big 5)
The system will evaluate users across five key dimensions:
*   **Openness**: Receptivity to new experiences and ideas.
*   **Conscientiousness**: Level of organization and dependability.
*   **Risk-taking**: Propensity for high-stakes vs. safe choices.
*   **Emotional Stability**: Consistency in responses under pressure.
*   **Decision Speed**: Efficiency and hesitation in cognitive tasks.

### 2. Micro-Question Set (Draft)
The initial assessment consists of 35 tasks:
*   **10 Binary Choices**: Preference-based questions (e.g., "Plan" vs. "Spontaneity").
*   **10 Reaction-Speed Tasks**: Rapid-fire visual or text cues.
*   **10 Short Text Prompts**: Open-ended responses for NLP analysis.
*   **5 Confidence-Scale Questions**: Self-assessment of choice certainty.

### 3. Database Schema (SQLite)
```sql
CREATE TABLE user_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    question_id INTEGER,
    answer TEXT,
    reaction_time_ms INTEGER,
    confidence_score INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 4. System Architecture
**Flutter (Frontend)** → **FastAPI (Backend)** → **ML Models (Scikit-learn/XGBoost/S-BERT)** → **Insightful Response**

---
*This document marks the completion of Day 1.*
