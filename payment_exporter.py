import uuid
import logging


def payment_exporter():
    """ system to export the payment proofs to whatever system. For now returns uuid as 'key' """
    logging.info('received payment')
    return str(uuid.uuid4())
