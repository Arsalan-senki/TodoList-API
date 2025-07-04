from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app import models
from app.database import engine
from app.routers import tasks
from app.logger import logger

# Create tables
models.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(
    title="Todo List",
    description="A simple todo list API",
    version="1.0.0"
)

# Include router
app.include_router(tasks.router)

# Global exception handler for uncaught exceptions
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error at {request.url.path}: {repr(exc)}")
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"},
    )

# Global exception handler for SQLAlchemy-related errors
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"Database error at {request.url.path}: {repr(exc)}")
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Database error"},
    )
