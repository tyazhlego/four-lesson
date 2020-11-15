if __name__ == '__main__':
    pass


import os
import logging
import time
import requests


from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

logging.basicConfig(filename='logg.log', level=logging.INFO)

def api_check():
    while True:
        try:
            response = requests.get('http://ya.ru/')
            logging.info('запрос к серверу....')
        except:
            logging.warning('ошибка!')
            client.messages.create(
                body='Ошибка в мониторинге',  # текст сообщения
                from_='19378216672',  # номер, который был получен
                to='79951123345',  # твой номер, на который придёт sms
                )
            time.sleep(60)
            exit
        else:
            if response.status_code == 200:
                logging.info('всё хорошо')
            else:
                logging.error('все сломалось!')
                client.messages.create(
                body='Ошибка в мониторинге',  # текст сообщения
                from_='19378216672',  # номер, который был получен
                to='79951123345',  # твой номер, на который придёт sms
                )
            time.sleep(60)


api_check()