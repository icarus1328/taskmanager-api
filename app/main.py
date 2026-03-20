from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

app = FastAPI()

#UserCreate
@app.post('/users', response_model= schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(db_get)):
    if db.query(models.User).filter(models.User.username == user.username):
        return HTTPException(status_code=400, detail="Username already exists!")
    
    db_user = models.User(username= user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user