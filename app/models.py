from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, BigInteger
from sqlalchemy.orm import relationship
from app.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created = Column(BigInteger, nullable=False)

    portfolio = relationship("PortfolioDB", back_populates="user", cascade="all, delete-orphan")
    favorites = relationship("FavoriteDB", back_populates="user", cascade="all, delete-orphan")
    alerts = relationship("AlertDB", back_populates="user", cascade="all, delete-orphan")

class PortfolioDB(Base):
    __tablename__ = "portfolio"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    coin_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    ts = Column(BigInteger, nullable=False)

    user = relationship("UserDB", back_populates="portfolio")

class FavoriteDB(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    coin_id = Column(String, nullable=False)

    user = relationship("UserDB", back_populates="favorites")

class AlertDB(Base):
    __tablename__ = "alerts"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sym = Column(String, nullable=False)
    cid = Column(String, nullable=False)
    dir = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    via = Column(String, nullable=False) # через запятую храним каналы (br,tg,em)
    done = Column(Boolean, default=False)
    ts = Column(BigInteger, nullable=False)

    user = relationship("UserDB", back_populates="alerts")