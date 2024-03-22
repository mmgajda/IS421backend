from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
import datetime

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
