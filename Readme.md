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
```
pip install -r requirements.txt
```

### Running the code
Generate an empty database with
```
python manage.py create_db
```

Fill it with some sample data
```
python manage.py create_sample_data
```

Start the API which will listen on http://localhost:5000/
```
python api.py
```

### Features
The database contains 3 tables:
```
partners:
	account_id -> string
	name -> string
	create_date -> datetime (autofill)
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
    payment_received_date -> DateTime  # when our system got the notification
    payment_processed_date -> DateTime  # date of payment routed to the partner service
```

## Authors

* **Daniel Lingvay** - *Initial work*