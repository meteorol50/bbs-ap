from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import sessionmaker

import app.cruds.post as post_crud
from app.db import get_db

from app.schemas.post import PostRequest, PostResponse

router = APIRouter()

@router.get("/", response_model = List[PostResponse])
async def home(db: sessionmaker = Depends(get_db)):
  return await post_crud.get_posts_with_user(db)

@router.post("/post", response_model = PostResponse)
async def post(post: PostRequest, db: sessionmaker = Depends(get_db)):
  return await post_crud.create_post(db, post)
