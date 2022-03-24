import requests
import os

def get_token(path: str) -> str:
    '''Функция считывает токен из текстового файла по указанному пути'''
    path_to_token = input('Enter path to file with token: ')
    try:
        with open(path, 'r') as f:
            token = f.readline()
    except FileNotFoundError:
        print("File with token is not found")
    return token

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
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
    TOKEN_PATH = os.path.join(os.getcwd(), 'token.txt')
    path_to_file = input('Enter path to file you want upload: ')
    ya = YaUploader(get_token(TOKEN_PATH))
    ya.upload(path_to_file)
