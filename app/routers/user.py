from app.models.model import User
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from typing import Optional

import app.cruds.user as user_crud
from app.db import get_db
from app.schemas.user import UserRequest, UserResponse
from app.utils.authentication import check_signed_in

router = APIRouter()

@router.get("/user/{user_id}", response_model = UserResponse)
def get_profile(user_id: int, auth_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):
  check_signed_in(auth_token, db)

  user = user_crud.get_user_by_id(db, user_id)
  if user is None:
    raise HTTPException(status_code = 404, detail = "Not Found.")
  if user.name is None:
    user.name = ""
  return user

@router.post("/user/{user_id}", response_model = UserResponse)
def update_profile(
  user_id: int, userReqest: UserRequest, auth_token: Optional[str] = Cookie(None), db: Session = Depends(get_db)):

  check_signed_in(auth_token, db)

  user = user_crud.get_user_by_id(db, user_id)
  if user is None:
    raise HTTPException(status_code = 404, detail = "Not Found.")

  user.name = userReqest.name
  return user_crud.update_user(db, user)
