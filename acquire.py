import requests
import pandas as pd


def get_star_wars_all(base_url): 

    for i in range(1,10):
    
        response = requests.get(base_url) 
        data = response.json()
        df = pd.DataFrame(data['results'])
        next_page = data['next']
    
        while next_page is not None:
    
            new_url = base_url + f'{i}/'
            response_i = requests.get(new_url)
            data_i = response_i.json()

            #put new data into new df and concat with og df
            df_i = pd.DataFrame(data_i['results'])
            df = pd.concat([df, df_i], axis = 0)

            if next_page is None:
                break