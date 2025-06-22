from fastapi import FastAPI
from .routers import ingest, ask

app = FastAPI(title="Digital Mentor")

app.include_router(ingest.router)
app.include_router(ask.router)
