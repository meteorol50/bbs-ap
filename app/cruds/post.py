from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import app.models.model as post_model
import app.schemas.post as post_schema

async def create_post(
  db: AsyncSession, post_create: post_schema.PostRequest
) -> post_model.Post:
  post = post_model.Post(**post_create.dict())
  db.add(post)
  await db.commit()
  await db.refresh(post)
  return post

async def get_posts_with_user(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
  result: Result = await (
    db.execute(
      select(
        post_model.post.user_id,
        post_model.post.title.isnot(None),
        post_model.post.content.isnot(None),
      ).outerjoin(post_model.Done)
    )
  )
  return result.all()
