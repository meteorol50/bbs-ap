from fastapi import APIRouter

from app.schemas.post import Post

router = APIRouter()

@router.get("/")
async def home():
  pass

@router.post("/post")
async def post(post: Post):
  pass
