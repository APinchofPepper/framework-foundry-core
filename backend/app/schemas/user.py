from pydantic import BaseModel, EmailStr


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

    class Config:
        from_attributes = True
