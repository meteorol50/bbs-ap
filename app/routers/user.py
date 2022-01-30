from fastapi import APIRouter

from app.schemas.user import UserRequest, UserResponse

router = APIRouter()

@router.get("/user/{user_id}", response_model = UserResponse)
async def profile(user_id: int):
  user = UserResponse(user_id = user_id, name = "")
  return user

@router.post("/user/{user_id}", response_model = UserResponse)
async def edit_profile(user_id: int, user: UserRequest):
  result = UserResponse(user_id = user_id, **user.dict())
  return result
