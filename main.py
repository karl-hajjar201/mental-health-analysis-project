from fastapi import FastAPI
from endpoints import router
from seed_db import seed_db

app = FastAPI(title="Mental Health Insights API")

app.include_router(router)


@app.on_event("startup")
def startup_event():
    seed_db()
