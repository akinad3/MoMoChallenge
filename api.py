from common import payment_store
from models import Payers, Partners, Payments
from flask import Flask, request, Response
from db_connection import session

app = Flask(__name__)


@app.route("/africa_bank", methods=['POST'])
def africa_bank():
    if request.headers['Content-Type'] == 'application/json':
        json_object = request.json
        storage_key = payment_store(json_object)
        partner = session.query(Partners).get(json_object['account_number'])
        if not partner:
            # we can handle this, throwing logging etc here
            return Response('Account number not registered', status=500)
        payer = session.query(Payers).get(json_object['reference_number'])
        if not payer:
            # we can handle this to create a new payer with this reference number, throwing logging etc here
            return Response('Reference number not registered', status=500)
        session.add(Payments(partner=partner,
                             payer=payer,
                             amount=json_object['amount'],
                             currency=json_object['currency'],
                             # payment_date=json_object['payment_date'],
                             proof_key=storage_key))
        session.commit()
        return Response('Success', status=200)
    else:
        return '415 Unsupported Content-Type'


if __name__ == '__main__':
    app.run(debug=True)
