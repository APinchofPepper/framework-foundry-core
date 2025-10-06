from datetime import timedelta

from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.crud.user import (
    authenticate_user_by_email_or_username,
    create_user,
    get_user_by_email,
)
from app.db import get_db
from app.schemas.user import UserCreate, UserLogin, UserOut
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(
        db,
        email=user_in.email,
        password=user_in.password,
        full_name=user_in.full_name,  # noqa: E501
    )
    return user


@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    # Use email if provided, otherwise use username
    email_or_username = user_in.email or user_in.username
    user = authenticate_user_by_email_or_username(
        db, email_or_username, user_in.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",  # noqa: E501
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": token, "token_type": "bearer"}
