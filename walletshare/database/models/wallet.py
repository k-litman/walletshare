from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class Wallet(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    accounts = relationship('Account', back_populates='wallet')
    transactions = relationship('Transaction', back_populates='wallet')
