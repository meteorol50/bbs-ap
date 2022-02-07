from app.schemas.user import UserResponse
from app.utils.cryptography import decrypt
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

import app.cruds.user as user_crud
from app.db import Session, get_db
from app.schemas.auth import AuthRequest

from app.utils.authentication import create_auth_token

router = APIRouter()

@router.post("/signup", response_model = UserResponse)
def signup(auth: AuthRequest, db: Session = Depends(get_db)):
  user = user_crud.create_user(db, auth)
  if user.name is None:
      user.name = ""
  return user

@router.post("/signin", response_model = UserResponse)
def signin(auth: AuthRequest, response: Response, db: Session = Depends(get_db)):
  user = user_crud.get_user_by_email(db, auth.email)
  if user == None:
    raise HTTPException(status_code = 403, detail="Not Found.")
  elif auth.password != decrypt(user.password):
    raise HTTPException(status_code = 403, detail="Password is not correct.")

  if user.name is None:
    user.name = ""

  auth_token = create_auth_token(user, db)
  response.set_cookie(key="auth_token", value=auth_token)
  return user
