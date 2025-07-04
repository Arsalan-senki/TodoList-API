from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app import models, schemas


def get_all_tasks(db: Session):
    """
    Retrieve all tasks from the database.
    """
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int):
    """
    Retrieve a single task by its ID.
    """
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task_data: schemas.TaskCreate):
    """
    Create a new task using the provided schema data.
    """
    try:
        new_task = models.Task(**task_data.model_dump())
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def update_task(db: Session, task_id: int, task_data: schemas.TaskUpdate):
    """
    Update an existing task with the provided data.
    Returns the updated task, or None if not found.
    """
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if task is None:
            return None

        for k, v in task_data.model_dump(exclude_unset=True).items():
            setattr(task, k, v)

        db.commit()
        db.refresh(task)
        return task
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_task(db: Session, task_id: int):
    """
    Delete a task by its ID.
    Returns the deleted task, or None if not found.
    """
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if task is None:
            return None

        db.delete(task)
        db.commit()
        return task
    except SQLAlchemyError as e:
        db.rollback()
        raise e
