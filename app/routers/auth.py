from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

import app.cruds.user as user_crud
from app.db import Session, get_db
from app.schemas.auth import AuthRequest

router = APIRouter()

@router.post("/signup")
def signup(auth: AuthRequest, db: Session = Depends(get_db)):
  return user_crud.create_user(db, auth)

@router.post("/signin")
def signin(auth: AuthRequest, db: Session = Depends(get_db)):
  user = user_crud.get_user_by_email(db, auth.email)
  if user == None:
    raise HTTPException(status_code = 403, detail="Not Found.")
  elif auth.password != user.password:
    raise HTTPException(status_code = 403, detail="Password is not correct.")
  else:
    return user
