from pydantic import BaseModel

from walletshare.app.models.item import Item


class PositionBase(BaseModel):
    name: str
    cost: int
    quantity: int


class Position(PositionBase):
    id: int
    transaction_id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
