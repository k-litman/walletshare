from pydantic import BaseModel


class ItemBase(BaseModel):
    quantity: int


class Item(ItemBase):
    user_id: int
    wallet_id: int
    position_id: int

    class Config:
        orm_mode = True
