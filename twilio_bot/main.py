from twilio.rest import Client
from schedule import every, repeat, run_pending
import os
import time
import logging

logging.basicConfig(level=logging.INFO)


ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
TO_NUMBER = os.environ.get('TO_NUMBER')
FROM_NUMBER = os.environ.get('FROM_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)
client.http_client.logger.setLevel(logging.INFO)


@repeat(every(2).minutes.at(':30'))
def send_message():
    client.messages.create(
        to=TO_NUMBER,
        from_=FROM_NUMBER,
        body='This is a test. Please ignore.'
    )


if __name__ == '__main__':
    logging.info('We are online!')

    while True:
        run_pending()
        time.sleep(1)
