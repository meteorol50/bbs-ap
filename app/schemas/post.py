import string
from typing import Optional

from pydantic import BaseModel, Field

class Post(BaseModel):
  user_id: int
  title: str
  content: str
