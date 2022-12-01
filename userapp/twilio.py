import os

from django.conf import settings
from twilio.rest import Client
from VEGIE_PROJECT import settings
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


class MessageHandler:
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages \
            .create(
                body=f'Your otp is {self.otp}',
                from_='+18584655732',
                to=self.phone_number
            )

        print(message.sid)
