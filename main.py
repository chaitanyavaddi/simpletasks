from fastapi import FastAPI
from src.tasks import router as task_router

app = FastAPI()

app.include_router(task_router)
