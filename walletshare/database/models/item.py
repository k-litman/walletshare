from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class Item(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), primary_key=True)
    position_id = Column(Integer, ForeignKey('position.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)

    account = relationship('Account', back_populates='items')
    position = relationship('Position', back_populates='items')