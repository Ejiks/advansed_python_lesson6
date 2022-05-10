import requests
from pprint import pprint

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ''
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    response = requests.put(f'{URL}?path={path}', headers=headers)
    return response.status_code

def list_folder():
    response = requests.get(f'{URL}?path=%2Fhelo%20wolrd&fields=name', headers=headers)
    return response.json()

if __name__ == '__main__':
    create_folder = print(create_folder('helo wolrd'))
    list_folder = print(list_folder())



