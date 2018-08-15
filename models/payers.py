from sqlalchemy import Column, String, DateTime
from db_connection import Base
import datetime


class Payers(Base):
    __tablename__ = 'payers'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    create_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
