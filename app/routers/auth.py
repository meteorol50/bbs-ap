from fastapi import APIRouter

from app.schemas.auth import AuthRequest

router = APIRouter()

@router.post("/signup")
async def signup(auth: AuthRequest):
  pass

@router.post("/signin")
async def signin(auth: AuthRequest):
  pass

@router.post("/logout")
async def logout():
  pass
