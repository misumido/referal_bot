from sqlalchemy import (Column, Integer,
                        String, ForeignKey, Float, DateTime, Boolean)
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    tg_id = Column(Integer, unique=True)
    user_name = Column(String)
    balance = Column(Float, default=0.00)
    paid = Column(Float, default=0.00)
    refs = Column(Integer, default=0)
    invited = Column(String, default="Никто")
    invited_id = Column(Integer, nullable=True, default=None)
    banned = Column(Boolean, default=False)
    reg_date = Column(DateTime)

# в чистом проекте можно переделать чекер и добавить его в юзер
class Checker(Base):
    __tablename__ = "checker"
    ref_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    tg_id = Column(Integer, unique=True)
    inv_id = Column(Integer)
    add = Column(Boolean, default=False)


class Withdrawals(Base):
    __tablename__ = "withdrawal"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(Integer, ForeignKey("user.tg_id"))
    amount = Column(Float)
    card = Column(String)
    bank = Column(String)
    status = Column(String, default="ожидание")
    reg_date = Column(DateTime)


    user_fk = relationship(User, lazy="subquery")

class Channels(Base):
    __tablename__ = "channel"
    id = Column(Integer, primary_key=True, autoincrement=True)
    channel_url = Column(String, unique=True)
    channel_id = Column(Integer, unique=True)
    admins_channel = Column(Boolean, default=False)

class AdminInfo(Base):
    __tablename__ = "price"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, default=4.00)
    min_amount = Column(Float, default=60.00)
    admin_channel = Column(String)






