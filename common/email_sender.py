import smtplib
import json


class EmailServer():
    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.login("youremailusername", "password")

    def send_email(self, data):
        ''' obviously some error handling needed in case of connection drop etc.
            Currently sends a json dump of the as_dict_for_partner'''
        msg = json.dumps(data)
        self.server.sendmail("you@gmail.com", "target@example.com", msg)
