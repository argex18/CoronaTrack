from time import sleep

from CoronaTrack.scrape_data import scrape_data
from CoronaTrack.create_json import create_json

def main():
    data = scrape_data()
    fjson = create_json(data, 'Data/data.json')
if __name__ == '__main__':
    while True:
        main()
        break
        #sleep(3600)