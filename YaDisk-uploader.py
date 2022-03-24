import requests
import os

def _get_token() -> str:
    '''Функция считывает токен из текстового файла по указанному пути. 
       Проверок на правильность ввода не делал'''
    path_to_token = input('Enter path to file with token: ')
    with open(path_to_token, 'r') as f:
            token = f.readline()
    return token

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        '''Загрузчик. Проверок на правильность ввода не делал.'''
        response = requests.get(url='https://cloud-api.yandex.net/v1/disk/resources/upload',
                headers={'Authorization': 'OAuth ' + self.token},
                params={'path': os.path.basename(file_path), 'overwrite': 'true'},)
        response.raise_for_status()
        
        href = response.json()['href']

        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success!")

if __name__ == '__main__':
    path_to_file = input('Enter path to file you want upload: ')
    ya = YaUploader(_get_token())
    ya.upload(path_to_file)
    