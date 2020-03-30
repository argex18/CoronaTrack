from time import sleep

from CoronaTrack.scrape_data import scrape_data
from CoronaTrack.create_json import create_json
from CoronaTrack.get_credentials import __get_credentials
import CoronaTrack.send_email as email

def main():
    data = scrape_data()
    fjson = create_json(data, 'Data/data.json')
    email.send_message(__get_credentials('client_secret.json', 'token.pickle'), 'me', email.create_message_with_attachment(
        input('sender: '),
        input('receiver: '),
        email.subject,
        email.body_text,
        'Data/data.json'
    ))
if __name__ == '__main__':
    while True:
        main()
        break
        sleep(3600)