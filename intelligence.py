import requests

API = 'https://superheroapi.com/api/2619421814940190/'

def get_hero(competitors: list) -> str:
    for hero in heroes_list:
        for result in requests.get(API + f'/search/{hero}').json()['results']:
            superheroes[hero] = int(result['powerstats']['intelligence'])
    winner =  max(superheroes, key=superheroes.get)
    return f'The Winner is {winner} with intelligence {superheroes[winner]}'

if __name__ == '__main__':
    superheroes = {}
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    print(get_hero(heroes_list))

