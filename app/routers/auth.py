from fastapi import APIRouter

from app.schemas.auth import Auth

router = APIRouter()

@router.get("/signup")
async def show_signup():
  pass

@router.post("/signup")
async def signup(auth: Auth):
  pass

@router.get("/signin")
async def show_signin():
  pass

@router.post("/signin")
async def signin(auth: Auth):
  pass

@router.post("/logout")
async def logout():
  pass
