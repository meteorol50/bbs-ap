import string
from typing import Optional

from pydantic import BaseModel, Field

class Auth(BaseModel):
  email: str
  password: str
