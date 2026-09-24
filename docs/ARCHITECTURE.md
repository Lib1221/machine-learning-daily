# Architecture

Cognitive Echo scores personality and behavior traits from short interactive tasks.

```
Flutter client (planned) -> FastAPI backend -> SQLite -> feature extraction -> ML models -> insight report
```

## Backend (`backend/app.py`)

- FastAPI app with CORS open for the Flutter client.
- SQLite database `cognitive_echo.db`, created automatically with `user_responses` (user_id, question_id, answer, reaction_time_ms, confidence_score, timestamp).
- Endpoints: `POST /submit-response`, `GET /user-summary/{user_id}`, `GET /health`.

## Planned ML layer

- Features: answer patterns, reaction-time statistics, confidence calibration, text embeddings (S-BERT) for free-text prompts.
- Models: scikit-learn / XGBoost regressors per trait (Openness, Conscientiousness, Risk-taking, Emotional Stability, Decision Speed).

## Daily cadence

`daily_update.sh` commits and pushes with a timestamp, appending to `daily_log.txt`. Day-by-day notes live in [`PROJECT_PLAN.md`](guides/PROJECT_PLAN.md) and `DAY_N_PROGRESS.md`.
