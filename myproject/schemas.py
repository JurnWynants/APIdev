from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str

class Item(ItemBase):
    id: int
    owner_id: str

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass


class UserBase(BaseModel):
    email: str


class User(UserBase): # USER OUT
    id: int
    is_active: bool
    items:list[Item] = []


class UserCreate(UserBase): # USER IN
    password: str