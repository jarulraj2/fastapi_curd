from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
