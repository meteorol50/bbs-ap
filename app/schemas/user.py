import string
from pydantic import BaseModel, Field

class UserBase(BaseModel):
  name: str = Field("", max_length = 20)

class UserRequest(UserBase):
  pass

class UserResponse(UserBase):
  user_id: int
