from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    
class UserCreate(BaseModel):
    id: int
    username: str
    email: str

class TaskCreate(BaseModel):
    title: str
    completed: bool
    due_date: datetime
    user_id: int
    
class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool
    due_date: datetime
    
class TaskResponse(BaseModel):
    id: int
    title: str
    decription: str
    completed: bool
    due_date: datetime
    created_at: datetime
    updated_at: datetime
    user_id: int
    
class config:
    from_attributes = True