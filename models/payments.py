from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from db_connection import Base
from sqlalchemy.orm import relationship, backref
import datetime


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    reference_number = Column(String, ForeignKey('payers.id'), nullable=False)
    account_number = Column(String, ForeignKey('partners.account_id'), nullable=False)
    amount = Column(Integer, nullable=False)
    currency = Column(String, nullable=False)
    proof_key = Column(String, nullable=False)  # eg. key to S3 or some storage to keep the original proof
    payment_bank_date = Column(DateTime)  # date of bank transfer
    payment_received_date = Column(DateTime, default=datetime.datetime.now, nullable=False)  # when our system got the notification
    payment_processed_date = Column(DateTime)  # date of payment routed to the partner service
    partner = relationship("Partners", backref=backref('payments'))
    payer = relationship("Payers", backref=backref('payments'))
