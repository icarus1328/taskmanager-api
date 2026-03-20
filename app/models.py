from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    email    = Column(String(100), nullable=False, unique=True)
    
    tasks = relationship("Tasks", back_populates="author", cascade="all, delete-orphan") #when a user is deleted it automatically deletes related tasks instead of setting user id to NULL
    
    def __repr__(self):
        return f"<User ID: {self.user_id} Username: {self.username}"
    
class Tasks(Base):
    __tablename__ = 'tasks'
    
    id          = Column(Integer, primary_key=True, nullable=False,index=True)
    title       = Column(String(150), nullable=False)
    description = Column(String(200), nullable=True)
    completed   = Column(Boolean, default=False)
    due_date    = Column(DateTime(timezone=True), nullable=False)
    created_at  = Column(DateTime(timezone=False), server_default=func.now())
    updated_at  = Column(DateTime(timezone=False), server_default=func.now())
    user_id  = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    author = relationship("User", back_populates="tasks")
    
    def __repr__(self):
        return f"<Task: {self.title} Completed:{self.completed}>"
    
