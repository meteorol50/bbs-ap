from fastapi import HTTPException
from typing import Optional
import uuid

from app.cruds.user import get_user_by_auth_token, update_user
from app.db import Session
from app.models.model import User

def create_auth_token(user: User, db: Session) -> str:
  auth_token = str(uuid.uuid4())
  user.auth_token = auth_token
  update_user(db, user)
  return auth_token

def check_signed_in(auth_token: Optional[str], db: Session):
  if not is_signed_in(auth_token, db):
    raise HTTPException(status_code = 403, detail = "Have no Permission.")

def is_signed_in(auth_token: Optional[str], db: Session) -> bool:
  if auth_token is None:
    return False

  user = get_user_by_auth_token(db, auth_token)
  if user is None:
    return False

  return True