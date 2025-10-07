from app.core.dependencies import get_current_user
from app.core.logging import log_info
from app.schemas.user import UserOut
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_users_me(current_user=Depends(get_current_user)):
    log_info(f"User profile accessed: {current_user.email}")
    return current_user
