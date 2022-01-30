from typing import List

from fastapi import APIRouter

from app.schemas.post import PostRequest, PostResponse

router = APIRouter()

@router.get("/", response_model = List[PostResponse])
async def home():
  posts = [PostResponse]
  return posts

@router.post("/post", response_model = List[PostResponse])
async def post(post: PostRequest):
  posts = [PostResponse]
  return posts
