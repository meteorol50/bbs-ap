from typing import List, Tuple, Optional

from sqlalchemy.orm import Session
from sqlalchemy.engine.base import Engine

import app.models.model as user_model
import app.schemas.auth as auth_schema
import app.schemas.user as user_schema

def create_user(
  db: Session, user_create: auth_schema.AuthRequest
) -> user_model.User:
  user = user_model.User(**user_create.dict())
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_id(db: Session, user_id: int) -> Optional[user_model.User]:
  user: Optional[Tuple[user_model.User]] = db.query(user_model.User).filter(user_model.User.user_id == user_id).first()
  return user if user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

def get_user_by_email(db: Session, email: str) -> Optional[user_model.User]:
  user: Optional[Tuple[user_model.User]] = db.query(user_model.User).filter(user_model.User.email == email).first()
  return user if user is not None else None

# async def get_users(db: sessionmaker) -> List[Tuple[int, str]]:
#   return await db.query(user_model.User.user_id, user_model.User.name).all()

def update_user(
  db: Session, user_create: user_schema.UserRequest, original: user_model.User
) -> user_model.User:
  original.name = user_create.name
  db.add(original)
  db.commit()
  db.refresh(original)
  return original
