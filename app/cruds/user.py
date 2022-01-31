from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import app.models.model as user_model
import app.schemas.auth as auth_schema
import app.schemas.user as user_schema


async def create_user(
  db: AsyncSession, user_create: auth_schema.AuthRequest
) -> user_model.User:
  user = user_model.User(**user_create.dict())
  db.add(user)
  await db.commit()
  await db.refresh(user)
  return user

async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[user_model.User]:
  result: Result = await db.execute(
    select(user_model.User).filter(user_model.User.user_id == user_id)
  )
  user: Optional[Tuple[user_model.User]] = result.first()
  return user[0] if user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[user_model.User]:
  result: Result = await db.execute(
    select(user_model.User).filter(user_model.User.email == email)
  )
  user: Optional[Tuple[user_model.User]] = result.first()
  return user[0] if user is not None else None

async def get_users(db: AsyncSession) -> List[Tuple[int, str]]:
  result: Result = await (
    db.execute(
      select(
        user_model.User.user_id,
        user_model.User.name,
      )
    )
  )
  return result.all()

async def update_user(
  db: AsyncSession, user_create: user_schema.UserRequest, original: user_model.User
) -> user_model.User:
  original.name = user_create.name
  db.add(original)
  await db.commit()
  await db.refresh(original)
  return original
