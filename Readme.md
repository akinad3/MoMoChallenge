# MoMo application

Code challange application

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Application built around a small Flask API, SQLLite in-file database and SQLAlchemy ORM.

### Prerequisites

You probably want to install this inside a virtualenv. I'm using virtualenv and virtualenvwrapper.
http://roundhere.net/journal/virtualenv-ubuntu-12-10/

### Installing

After creating the virtualenv, you need to install the requirements.

```pip install -r requirements.txt``` to install pip packages

```python manage.py create_db``` to create an empty database

```python manage.py create_sample_data``` to fill it with some sample data

## Design
The database contains 3 tables:
```
partners:
    account_id -> string
    name -> string
    create_date -> datetime (autofill)
    notify_method -> string (eg. 'api', 'email' etc. Can be modified to have a hardcoded possibilities mapped to integers)
    contact_path -> string (used for url in case of apis, email addresses in case of email etc.)
payers:
    id -> string
    name -> string
    create_date -> datetime (autofill)
payments:
    id -> int
    reference_number -> string, foreign key to payers.id
    account_number -> string, foreign key to partners.account_id
    amount -> int
    currency -> string
    proof_key -> int     # key to S3 or some storage to keep the original proof
    payment_bank_date -> DateTime  # date of bank transfer
    payment_received_date -> DateTime  (autofill) # when our system got the notification
    payment_processed_date -> DateTime  # date of payment routed to the partner service
    process_error -> bool # in case of process_error, mark this as errored-out so the payment router won't try to process this again
```

### Incoming data:
A sample integration is a Flask REST API endpoint, where a bank can POST a payment.
```
python api.py
```
With the api running:
```
curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/africa_bank -d '{"reference_number":"payer1", "account_number":"partner1", "amount": "55", "currency": "USD"}'
``` 
This will create a Payment object, and a payment row in the database, linking the reference number / account number.
There is a function called, which can save the request / proof etc to a cloud-based service (eg. S3) and store the key of this to the payment object. 
Also some basic error-handling is implemented to throw errors in case of unknown reference number / account number.

### Outgoing data:
A sample daemon router is writter, which can be run in supervisor or whatever process handling package is used.
```
python manage.py run_payment_processor
```
This daemon job looks for payments in payments table which weren't processed yet (filtering them on payment_processed_date and process_error) and processing them. Routes can be set for each partner. Now emails and an external API is supported.
Note: this is just sample code, as I didn't create an other API for payment processing or email username/password.

## Authors
**Daniel Lingvay**
