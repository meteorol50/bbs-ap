from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import app.cruds.user as user_crud
from app.db import get_db
from app.schemas.auth import AuthRequest

router = APIRouter()

@router.post("/signup")
async def signup(auth: AuthRequest, db: AsyncSession = Depends(get_db)):
  return await user_crud.create_user(db, auth)

@router.post("/signin")
async def signin(auth: AuthRequest, db: AsyncSession = Depends(get_db)):
  return await user_crud.get_user_by_email(db, auth)
