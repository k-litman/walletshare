from pydantic import BaseModel

from walletshare.app.models.account import Account


class UserBase(BaseModel):
    username: str
    bank_account_number: str | None
    phone_number: str | None


class UserCreateDTO(UserBase):
    password: str


class UserUpdateDTO(UserBase):
    password: str | None


class User(UserBase):
    id: int
    accounts: list[Account] = []

    class Config:
        orm_mode = True
