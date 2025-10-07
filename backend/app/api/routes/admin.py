from app.core.dependencies import get_current_admin
from app.core.logging import log_info
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/stats")
def get_stats(admin=Depends(get_current_admin)):
    log_info(f"Admin stats accessed by: {admin.email}")
    # placeholder example data
    return {"total_users": 42, "active_frameworks": 5, "pending_clients": 2}
