from pydantic import BaseModel, Field
from datetime import datetime

class PostBase(BaseModel):
  user_id: int
  title: str = Field(..., min_length = 1, max_length = 50)
  content: str = Field(..., min_length = 1, max_length = 100)

class PostRequest(PostBase):
  pass

class PostResponse(PostBase):
  date: datetime
