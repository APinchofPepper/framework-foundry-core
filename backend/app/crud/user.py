from app.core.security import get_password_hash, verify_password
from app.models import User
from sqlalchemy.orm import Session


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, email: str, password: str, full_name: str = None):
    hashed_pw = get_password_hash(password)
    db_user = User(email=email, hashed_password=hashed_pw, full_name=full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


def authenticate_user_by_email_or_username(
    db: Session, email_or_username: str, password: str
):
    """Authenticate user by either email or username."""
    user = get_user_by_email(db, email_or_username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
