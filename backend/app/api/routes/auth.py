from datetime import timedelta

from app.core.logging import log_error, log_info, log_warning
from app.core.notifications import send_email
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.core.utils import validate_email
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
    try:
        # 1️⃣ Validate email
        if not validate_email(user_in.email):
            log_warning(f"Registration failed: invalid email format: {user_in.email}")
            raise HTTPException(status_code=400, detail="Invalid email format")

        # 2️⃣ Check if user already exists
        existing_user = get_user_by_email(db, user_in.email)
        if existing_user:
            log_warning(
                f"Registration failed: email already registered: {user_in.email}"
            )
            raise HTTPException(status_code=400, detail="Email already registered")

        # 3️⃣ Create user
        user = create_user(
            db,
            email=user_in.email,
            password=user_in.password,
            full_name=user_in.full_name,
        )
        log_info(f"New user registered: {user.email}")

        # 4️⃣ Send welcome email (notification)
        try:
            send_email(
                user.email,
                "Welcome to Framework Foundry!",
                f"Hello {user.full_name}, welcome!",
            )
        except Exception as e:
            log_error(f"Failed to send welcome email to {user.email}: {e}")

        return user

    except HTTPException:
        # Re-raise HTTP exceptions as they are already handled
        raise
    except Exception as e:
        log_error(f"Unexpected error during registration for {user_in.email}: {e}")
        raise HTTPException(
            status_code=500, detail="Internal server error during registration"
        )


@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    try:
        # Use email if provided, otherwise use username
        email_or_username = user_in.email or user_in.username
        user = authenticate_user_by_email_or_username(
            db, email_or_username, user_in.password
        )

        if not user:
            log_warning(f"Failed login attempt: {email_or_username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        # 1️⃣ Create JWT token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        log_info(f"User logged in: {user.email}")

        # 2️⃣ Optional: send login notification
        try:
            send_email(
                user.email,
                "New Login Detected",
                f"Hello {user.full_name}, you just logged in.",
            )
        except Exception as e:
            log_error(f"Failed to send login notification to {user.email}: {e}")

        return {"access_token": token, "token_type": "bearer"}

    except HTTPException:
        # Re-raise HTTP exceptions as they are already handled
        raise
    except Exception as e:
        email_or_username = user_in.email or user_in.username
        log_error(f"Unexpected error during login for {email_or_username}: {e}")
        raise HTTPException(
            status_code=500, detail="Internal server error during login"
        )
