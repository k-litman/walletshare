from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class Account(BaseModel):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), primary_key=True)

    user = relationship('User', back_populates='accounts')
    wallet = relationship('Wallet', back_populates='accounts')
    items = relationship('Item', back_populates='account')
