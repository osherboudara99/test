from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4 # Universally Unique Identifier
from enum import Enum

class Gender(str, Enum): # creating class of appropriate values
    male = "male"
    female = "female"

class Role(str, Enum): # creating class with appropriate values
    admin = "admin"
    user = "user"
    student = "student"


# Table structured class
class User(BaseModel):
    id: Optional[UUID] = uuid4() # If not set, then an ID is generated
    first_name: str 
    last_name: str 
    middle_name: Optional[str] = None
    gender: Gender 
    roles: List[Role]



class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]

