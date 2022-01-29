import string
from typing import Optional

from pydantic import BaseModel, Field

class User(BaseModel):
  name: str
  email: str
  password: str
