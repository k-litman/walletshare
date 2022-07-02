from pydantic import BaseModel

from walletshare.app.models.item import Item


class AccountBase(BaseModel):
    pass


class Account(AccountBase):
    user_id: int
    wallet_id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
