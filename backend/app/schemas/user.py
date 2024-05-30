from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    user_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
