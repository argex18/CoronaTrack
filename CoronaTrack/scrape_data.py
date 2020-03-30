import bs4
import requests

def scrape_data():
    data = []
    try:
        page = requests.get('https://www.worldometers.info/coronavirus/#countries')
        soup = bs4.BeautifulSoup(page.text, 'html.parser')

        table = soup.find('table', id='main_table_countries_today')
        thead = table.find('thead')
        tbody = table('tbody')[0]

        i = 0
        for row in tbody('tr'):
            data.append({})
            for th in thead.find('tr')('th'):
                data[i].setdefault(th.text, None)
            for key, td in zip(data[i].keys(), row('td')):
                data[i][key] = td.text
            i = i + 1
        for state in data:
            print(state)
            print('\n===========================\n')
        
        return {"Outbreak": data}
    except Exception as err:
        print(err)
        return None

if __name__ == '__main__':
    scrape_data()