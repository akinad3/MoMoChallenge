from sqlalchemy.sql.expression import false  # avoid throwing PEP8 error
from common import EmailServer
from db_connection import session
from models import Payments
import requests
import datetime
import logging


class PaymentRouter():
    @classmethod
    def process(cls):
        email_sender = EmailServer()
        while True:
            session.commit()  # to refresh the transaction in case of multiple sessions,
                              # as long-living sessions/transactions won't detect changes
            unprocessed_payment = session.query(Payments)\
                                         .filter(Payments.process_error == false())\
                                         .filter(Payments.payment_processed_date.is_(None))\
                                         .first()
            try:
                # payment rounting by account account_number
                # Rounting can be done with multiple ways, stored in Partner.notify_method'''
                if unprocessed_payment.partner.notify_method == 'api':
                    requests.post(unprocessed_payment.partner.contact_path, data=unprocessed_payment.as_dict_for_partner())
                if unprocessed_payment.partner.notify_method == 'email':
                    email_sender.send_email(data=unprocessed_payment.as_dict_for_partner())
            except Exception as e:
                logging.error('error with payment id {0}. Error: {1}'.format(unprocessed_payment.id, e))
                unprocessed_payment.process_error = True
            else:
                unprocessed_payment.payment_processed_date = datetime.datetime.now()
            session.commit()
