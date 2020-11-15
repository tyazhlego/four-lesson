import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    body='ПРИВЕТ!!!',  # текст сообщения
    from_='19378216672',  # номер, который был получен
    to='79951123345',  # твой номер, на который придёт sms
    )

print(message.sid)