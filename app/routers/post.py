from typing import List, Optional
from app.utils.authentication import check_signed_in

from fastapi import APIRouter, Cookie, Depends, HTTPException
from sqlalchemy.orm import Session

import app.cruds.post as post_crud
from app.db import get_db

from app.schemas.post import PostRequest, PostResponse

router = APIRouter()

@router.get("/", response_model = List[PostResponse])
def home(auth_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):

  check_signed_in(auth_token, db)

  return post_crud.get_posts_with_user(db)

@router.post("/post", response_model = PostResponse)
def post(post: PostRequest, auth_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):

  check_signed_in(auth_token, db)

  return post_crud.create_post(db, post)
