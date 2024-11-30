from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    login: str = Field(..., min_length=4)
    password: str = Field(..., min_length=4)
    email: EmailStr

class ShowUser(BaseModel):
    id: int
    login: str