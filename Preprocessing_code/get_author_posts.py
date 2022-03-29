
import time
import requests
from psaw import PushshiftAPI
import pandas as pd

api = PushshiftAPI()


def get_data(label,author):
    
    if (label == 0):
        subreddit='nottheonion'
    elif (label == 1):
        subreddit='TheOnion'
        
    kwargs = {'author': author, 'subreddit': subreddit}
    r = requests.get("https://api.pushshift.io/reddit/submission/search/",params=kwargs)

    if r:        
        data = r.json()
        print(len(data['data']))
        return (len(data['data']))
    else:
        print('0')
        return ('0') 

df = pd.read_csv("preprocessed_nto_to.csv", low_memory=False)
df = df.reset_index()  # make sure indexes pair with number of rows   

df['author_number_of_posts'] = df.apply(lambda row: get_data(row['label'], row['author']), axis=1)

df.to_csv("processed_file_with_author_posts.csv")
