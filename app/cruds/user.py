from app.utils.cryptography import encrypt
from typing import Tuple, Optional

from sqlalchemy.orm import Session

from app.models.model import User
import app.schemas.auth as auth_schema

def create_user(
  db: Session, user_create: auth_schema.AuthRequest
) -> User:
  user = User(**user_create.dict())

  # パスワード暗号化
  user.password = encrypt(user.password)

  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
  user: Optional[Tuple[User]] = db.query(User).filter(User.user_id == user_id).first()
  return user if user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

def get_user_by_email(db: Session, email: str) -> Optional[User]:
  user: Optional[Tuple[User]] = db.query(User).filter(User.email == email).first()
  return user if user is not None else None

def get_user_by_auth_token(db: Session, auth_token: str) -> Optional[User]:
  user: Optional[Tuple[User]] = db.query(User).filter(User.auth_token == auth_token).first()
  return user if user is not None else None

# async def get_users(db: sessionmaker) -> List[Tuple[int, str]]:
#   return await db.query(User.user_id, User.name).all()

def update_user(
  db: Session, user: User
) -> User:
  db.add(user)
  db.commit()
  db.refresh(user)
  return user
