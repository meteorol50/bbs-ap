from typing import List
from datetime import datetime, timezone, timedelta
from sqlalchemy import desc

from sqlalchemy.orm import Session

from app.models.model import Post
import app.schemas.post as post_schema

def create_post(
  db: Session, post_create: post_schema.PostRequest
) -> Post:
  post = Post(**post_create.dict())
  post.date = datetime.now(timezone(timedelta(hours=9)))
  db.add(post)
  db.commit()
  db.refresh(post)
  return post

def get_posts_with_user(db: Session) -> List[Post]:
  return db.query(Post).order_by(desc(Post.date)).all()
