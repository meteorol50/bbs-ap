from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Auth(Base):
    __tablename__ = "auths"

    auth_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    email = Column(String(255), nullable=True)
    password = Column(String(60), nullable=True)

    user = relationship("User", back_populates="user")

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    title = Column(String(255), nullable=True)
    content = Column(String(1000), nullable=True)

    user = relationship("User", back_populates="user")
