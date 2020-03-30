import json
if __name__ == '__main__':
    from scrape_data import scrape_data

def create_json(data, file):
    jfile = None
    try:
        with open(file, 'wb') as f:
            f.write(json.dumps(data, sort_keys=True, indent=5).encode())
            jfile = f
    except Exception as err:
        jfile = err # Set the exception to jfile
    finally:
        return jfile # Return jfile in any case

if __name__ == '__main__':
    create_json(scrape_data(), '../Data/data.json')