from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, PastDate
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=80)
    email: EmailStr = Field(max_length=250)
    phone: PhoneNumber
    birthday: PastDate
    address: Optional[str] = Field(max_length=300)


class ContactResponse(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ContactUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50) 
    surname: Optional[str] = Field(None, max_length=80)
    email: Optional[EmailStr] = Field(None, max_length=250)
    phone: Optional[PhoneNumber] = None
    birthday: Optional[PastDate] = None
    address: Optional[str] = Field(None, max_length=300)

    @property
    def is_dirty(self) -> bool:
        return any(self.__dict__.values())
    

class UserModel(BaseModel):
    username: str = Field(min_length=2, max_length=16)
    email: str
    password: str = Field(min_length=4, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
