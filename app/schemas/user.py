from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
  name: Optional[str] = Field("", max_length = 20)

class UserRequest(UserBase):
  pass

class UserResponse(UserBase):
  user_id: int

  class Config:
    orm_mode = True
