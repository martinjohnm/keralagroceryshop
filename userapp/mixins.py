import django


from django.conf import settings
from twilio.rest import Client
import optparse


class MessageHandler:
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp
    def send_otp_on_phone(self):
        pass