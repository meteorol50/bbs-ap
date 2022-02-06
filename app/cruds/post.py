from typing import List, Tuple
from datetime import datetime, timezone, timedelta

from sqlalchemy.orm import Session

import app.models.model as post_model
import app.schemas.post as post_schema

def create_post(
  db: Session, post_create: post_schema.PostRequest
) -> post_model.Post:
  post = post_model.Post(**post_create.dict())
  post.date = datetime.now(timezone(timedelta(hours=9)))
  db.add(post)
  db.commit()
  db.refresh(post)
  return post

# async def get_posts_with_user(db: sessionmaker) -> List[Tuple[int, str, str, str]]:
#   return await db.query(
#     post_model.post.user_id,
#     post_model.post.title.isnot(None),
#     post_model.post.content.isnot(None),
#   ).outerjoin(post_model.Done).all()
