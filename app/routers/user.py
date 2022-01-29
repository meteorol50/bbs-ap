from fastapi import APIRouter

from app.schemas.user import User

router = APIRouter()

@router.get("/user/{user_id}")
async def profile(user_id: int):
  return {"user_id": user_id}

@router.post("/user/{user_id}")
async def edit_profile(user_id: int, user: User):
  result = {"user_id": user_id, **user.dict()}
  pass
