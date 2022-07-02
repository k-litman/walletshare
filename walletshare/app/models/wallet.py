from pydantic import BaseModel

from walletshare.app.models.transaction import Transaction


class WalletBase(BaseModel):
    name: str


class Wallet(WalletBase):
    id: int
    transactions: list[Transaction] = []

    class Config:
        orm_mode = True
