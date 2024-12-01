from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    password_confirm: str
    age: int

class User(BaseModel):
    id: int
    username: str
    age: int

    class Config:
        orm_mode = True

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float

    class Config:
        orm_mode = True
