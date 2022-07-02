from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class Position(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    transaction_id = Column(Integer, ForeignKey('transaction.id'), nullable=False)

    transaction = relationship('Transaction', back_populates='positions')
    items = relationship('Item', back_populates='position')