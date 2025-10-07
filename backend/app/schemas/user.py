from datetime import datetime

from pydantic import BaseModel, EmailStr, computed_field


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    password: str

    def model_post_init(self, __context) -> None:
        if not self.email and not self.username:
            raise ValueError("Either email or username must be provided")
        if self.email and self.username:
            raise ValueError("Provide either email or username, not both")


class UserOut(UserBase):
    id: int
    is_active: bool
    role: str
    created_at: datetime
    updated_at: datetime

    @computed_field
    @property
    def created_at_formatted(self) -> str:
        from app.core.utils import format_datetime

        return format_datetime(self.created_at)

    @computed_field
    @property
    def updated_at_formatted(self) -> str:
        from app.core.utils import format_datetime

        return format_datetime(self.updated_at)

    class Config:
        from_attributes = True
