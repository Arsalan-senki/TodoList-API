from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas, database

# Define API router with prefix and tags
router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    """
    Dependency for getting a DB session.
    Ensures proper session closing after use.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.TaskInDB])
def read_tasks(db: Session = Depends(get_db)):
    """
    Get all tasks from the database.
    """
    return crud.get_all_tasks(db)


@router.get("/{task_id}", response_model=schemas.TaskInDB)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Get a single task by ID.
    Raises 404 if not found.
    """
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.post("/", response_model=schemas.TaskInDB, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Create a new task.
    Returns the created task with ID and timestamp.
    """
    return crud.create_task(db, task)


@router.put("/{task_id}", response_model=schemas.TaskInDB)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    """
    Update an existing task by ID.
    Raises 400 if task does not exist.
    """
    updated = crud.update_task(db, task_id, task_data)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task not found"
        )
    return updated


@router.delete("/{task_id}", response_model=schemas.TaskInDB, status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Delete a task by ID.
    Raises 400 if task does not exist.
    """
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task not found"
        )
    return deleted
