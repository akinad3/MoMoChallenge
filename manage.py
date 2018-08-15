from manager import Manager
from models import *
from db_connection import *

manager = Manager()


@manager.command
def create_db():
    Base.metadata.create_all(engine)


@manager.command
def create_sample_data():
    session.add(Partners(account_id='partner1', name='partner1_name', notify_method='api'))
    session.add(Payers(id='payer1', name='payer1'))
    session.commit()


@manager.command
def run_payment_processor():
    from background_jobs import PaymentRouter
    PaymentRouter.process()


if __name__ == '__main__':
    manager.main()
