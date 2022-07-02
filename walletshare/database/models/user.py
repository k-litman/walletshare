from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from walletshare.database import BaseModel


class User(BaseModel):
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=True)
    bank_account_number = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)

    accounts = relationship('Account', back_populates='user')