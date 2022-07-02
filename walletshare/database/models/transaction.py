from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class Transaction(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), nullable=False)

    wallet = relationship('Wallet', back_populates='transactions')
    positions = relationship('Position', back_populates='transaction')
