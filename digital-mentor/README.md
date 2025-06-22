# Digital Mentor

A local AI assistant for the Akimat of Astana.

## Setup

1. Install Docker and Docker Compose.
2. Copy `.env.example` to `.env` and set values.
3. Run `docker-compose up --build`.

Development requires Python 3.11 and Node.js 18.

Example `.env`:

```
SECRET_KEY=change_me
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
REDIS_URL=redis://redis:6379/0
MODEL_PATH=/models/paraphrase-multilingual-MiniLM-L12-v2
```
