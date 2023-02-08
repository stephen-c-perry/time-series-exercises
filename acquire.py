import requests
import pandas as pd


def star_wars_people():
 
    url = 'https://swapi.dev/api/people'
    response = requests.get(url)
    data = response.json()
    people = pd.DataFrame(data['results'])
    
    while data['next'] != None:
        response = requests.get(data['next'])
        data = response.json()
        people = pd.concat([people,
                               pd.DataFrame(data['results'])],
                              ignore_index=True)
    
    return people




def star_wars_planets():
 
    url = 'https://swapi.dev/api/planets'
    response = requests.get(url)
    data = response.json()
    planets = pd.DataFrame(data['results'])
    
    while data['next'] != None:
        response = requests.get(data['next'])
        data = response.json()
        planets = pd.concat([planets,
                               pd.DataFrame(data['results'])],
                              ignore_index=True)
    
    return planets



def star_wars_starships():
 
    url = 'https://swapi.dev/api/starships'
    response = requests.get(url)
    data = response.json()
    starships = pd.DataFrame(data['results'])
    
    while data['next'] != None:
        response = requests.get(data['next'])
        data = response.json()
        starships = pd.concat([starships,
                               pd.DataFrame(data['results'])],
                              ignore_index=True)
    
    return starships



def get_all_star_wars():
    csv = pd.read_csv('all_star_wars.csv')
    return csv