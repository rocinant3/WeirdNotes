from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    password_hash: bytes
    password_salt: bytes
    token: str


class UserCreateSchema(UserBase):
    pass


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInSchema(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=7)


class UserOutSchema(BaseModel):
    id: int
    email: EmailStr
    token: str

    class Config:
        orm_mode = True
