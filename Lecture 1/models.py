from pydantic import BaseModel
from typing import Optional , List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    customer = 'customer'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    gender: Gender
    role: List[Role]
