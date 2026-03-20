from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, get_db

app = FastAPI()

#Creating User
@app.post('/users', response_model= schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists!")
    
    db_user = models.User(username= user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Fetching User by ID
@app.get('/users/{user_id}', response_model=schemas.UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return user

#Fetching all Users
@app.get('/users', response_model=list[schemas.UserResponse])
def get_users(db: Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users

#Deleting User
@app.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found!")
    db.delete(user)
    db.commit()
    return {"detail":"User Deleted Successfully."}

#Creating Task
@app.post('/tasks', response_model=schemas.TaskCreate)
def create_task(task: schemas.TaskCreate, db: Session=Depends(get_db)):
    if db.query(models.Tasks).filter(models.Tasks.title == task.title, models.Tasks.user_id == task.user_id).first():
        raise HTTPException(status_code=400, detail="Task already exists!")
    db_task=models.Tasks(title=task.title, description=task.description, completed=task.completed, due_date=task.due_date, user_id=task.user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    
    return db_task

#Fetching task by user ID
@app.get('/tasks/user/{userid}',response_model=list[schemas.TaskResponse])
def get_tasks_by_userid(userid:int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found!")
    db_tasks= user.tasks
    return db_tasks

#Fetching task by task ID
@app.get('/tasks/{task_id}', response_model=schemas.TaskResponse)
def get_task_by_id(task_id:int, db: Session=Depends(get_db)):
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    return task

#Updating Existing Task
@app.patch('/tasks/{task_id}',response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session=Depends(get_db)):
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    
    for field, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    
    return task

#Deleting a task
@app.delete('/tasks/{task_id}')
def delete_task(task_id: int, db:Session=Depends(get_db)):
    task = db.query(models.Tasks).filter(models.Tasks.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found!")
    db.delete(task)
    db.commit()
    
    return {"detail":"Task Deleted Successfully"}