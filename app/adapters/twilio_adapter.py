import os

from dotenv import load_dotenv
from twilio.rest import Client

from app.interfaces.sender_api import SenderInterface


load_dotenv()


class TwilioAdapter(SenderInterface):
    def __init__(self, account_sid, auth_token):
        self.cliente = Client(account_sid, auth_token)

    def send_message(selfe, destiny, message):
        twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
        message = selfe.cliente.messages.create(
            to=destiny,
            from_=twilio_whatsapp_number,
            body=message)
        return message.sid
