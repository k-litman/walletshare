from pydantic import BaseModel
from datetime import datetime

from walletshare.app.models.position import Position


class TransactionBase(BaseModel):
    name: str
    date: datetime


class Transaction(TransactionBase):
    id: int
    wallet_id: int
    positions: list[Position] = []

    class Config:
        orm_mode = True