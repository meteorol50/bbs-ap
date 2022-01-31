from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import sessionmaker

import app.cruds.user as user_crud
from app.db import get_db

from app.schemas.user import UserRequest, UserResponse

router = APIRouter()

@router.get("/user/{user_id}", response_model = UserResponse)
async def get_profile(user_id: int, db: sessionmaker = Depends(get_db)):
  return await user_crud.get_user_by_id(db, user_id)

@router.post("/user/{user_id}", response_model = UserResponse)
async def update_profile(user_id: int, userReqest: UserRequest, db: sessionmaker = Depends(get_db)):
  user = await user_crud.get_user_by_id(db, user_id)
  if user is None:
    raise HTTPException(status_code=404, detail="User not found")

  return await user_crud.update_user(db, userReqest, original=user)
