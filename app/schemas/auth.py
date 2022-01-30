from pydantic import BaseModel, Field, EmailStr

class AuthRequest(BaseModel):
  email: EmailStr
  password: str = Field(..., min_length = 8, max_length = 20)
