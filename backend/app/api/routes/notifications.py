from app.core.dependencies import get_current_user
from app.crud.notification import get_user_notifications, mark_as_read
from app.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", summary="Get unread notifications")
def list_notifications(
    current_user=Depends(get_current_user), db: Session = Depends(get_db)
):
    return get_user_notifications(db, user_id=current_user.id)


@router.post("/{notif_id}/read", summary="Mark notification as read")
def read_notification(
    notif_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    notif = mark_as_read(db, notif_id)
    if notif.user_id != current_user.id:
        return {"error": "Not allowed"}
    return notif
