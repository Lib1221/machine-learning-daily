# Cognitive Echo (machine-learning-daily)

A daily-build project: an AI personality and behavior analyzer that infers traits from interactive micro-tasks, reaction times, and short text answers. Progress is committed every day, and the daily logs in this repo document each step.

## What it does

Users complete a short assessment (binary choices, reaction-speed tasks, short text prompts, and confidence ratings). The backend records answers with reaction time and confidence, and ML models score five dimensions: Openness, Conscientiousness, Risk-taking, Emotional Stability, and Decision Speed.

## Architecture

```
Flutter (frontend)  ->  FastAPI (backend)  ->  ML models (scikit-learn / XGBoost / S-BERT)  ->  insight report
```

## Repository layout

```
backend/
├── app.py            # FastAPI app with SQLite storage
└── requirements.txt
PROJECT_PLAN.md       # Day 1: system design, question set, schema
DAY_2_PROGRESS.md     # Day 2: data collection engine
daily_update.sh       # Commit-and-push script used for daily updates
daily_log.txt         # Timestamped update log
```

## API (current)

| Method | Endpoint                   | Purpose                                              |
| ------ | -------------------------- | ---------------------------------------------------- |
| POST   | `/submit-response`         | Store an answer with reaction time and confidence    |
| GET    | `/user-summary/{user_id}`  | Aggregate stats for a user                           |
| GET    | `/health`                  | Health check                                         |

## Running the backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

The SQLite database (`cognitive_echo.db`) is created automatically on first run. Interactive docs are at `http://127.0.0.1:8000/docs`.

## Roadmap

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for the full plan and [DAY_2_PROGRESS.md](DAY_2_PROGRESS.md) for the latest completed milestone. Upcoming: feature extraction from responses, model training, and the Flutter client.
