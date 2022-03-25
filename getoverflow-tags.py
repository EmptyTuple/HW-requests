import requests
import datetime

def get_messages(tag: str):
    API = 'https://api.stackexchange.com/questions'

    # преобразуем даты в unix epoch time как того требует API
    now = str(int(datetime.datetime.now().timestamp()))
    twodaysago = str(int((datetime.datetime.now() - datetime.timedelta(hours=48)).timestamp()))
    params = {'pagesize': '100', 'fromdate': twodaysago, 'todate': now, 'sort': 'creation', 'tagged': f'{tag}', 'site': 'stackoverflow'}
    response = requests.get(url=API, params=params, timeout=10)
    response.raise_for_status()
    
    row_messages = response.json()['items']
    for line in row_messages:
        time_tag = str(datetime.datetime.utcfromtimestamp(line['creation_date']).strftime('%Y-%m-%d %H:%M:%S'))
        msg_tag = line['tags']
        msg_title = line['title']
        msg_link = line['link']
        print(f'{time_tag}\n{msg_tag}\n{msg_title}\n{msg_link}')
        print('-----------------------')

if __name__ == '__main__':
    get_messages('python')