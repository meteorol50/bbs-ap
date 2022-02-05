from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.cruds.user as user_crud
from app.db import Session, get_db
from app.schemas.auth import AuthRequest

router = APIRouter()

@router.post("/signup")
def signup(auth: AuthRequest, db: Session = Depends(get_db)):
  return user_crud.create_user(db, auth)

# @router.post("/signin")
# async def signin(auth: AuthRequest):
#   return await user_crud.get_user_by_email(db, auth)
