from typing import List, Tuple

from sqlalchemy.orm import sessionmaker

import app.models.model as post_model
import app.schemas.post as post_schema

async def create_post(
  db: sessionmaker, post_create: post_schema.PostRequest
) -> post_model.Post:
  post = post_model.Post(**post_create.dict())
  db.add(post)
  await db.commit()
  await db.refresh(post)
  return post

async def get_posts_with_user(db: sessionmaker) -> List[Tuple[int, str, str, str]]:
  return await db.query(
    post_model.post.user_id,
    post_model.post.title.isnot(None),
    post_model.post.content.isnot(None),
  ).outerjoin(post_model.Done).all()
