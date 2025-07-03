from fastapi import FastAPI
from app import models
from app.database import engine
from routers import tasks


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo List",
    description="A simple todo list API",
    version="1",
)

app.include_router(tasks.router)