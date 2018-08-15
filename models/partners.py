from sqlalchemy import Column, String, DateTime
from db_connection import Base
import datetime


class Partners(Base):
    __tablename__ = 'partners'
    account_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    create_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
