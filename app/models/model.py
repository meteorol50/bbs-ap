from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = ({"comment": "ユーザー"},)

    user_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    email = Column(String(255), nullable=False)
    password = Column(String(60), nullable=False)

class Post(Base):
  __tablename__ = "posts"

  post_id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
  title = Column(String(255), nullable=True)
  content = Column(String(1000), nullable=True)
  date = Column(DateTime, nullable=False)

  user = relationship("User", backref="posts")
