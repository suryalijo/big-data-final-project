
import time
from psaw import PushshiftAPI
import pandas as pd

api = PushshiftAPI()
subreddit='worldnews'
final_data = []

def get_data(after,before):    
    result =  list(api.search_submissions(subreddit=subreddit,
                            filter=['author','created_utc','id','num_comments',
                                    'score', 'title','url'],
                            after = after,
                            before = before,
                            limit=1000))
    #print(result)  
    return result

def add_to_list(results):
    interim_data = []
    for i in range(len(results)):
        scrape_dict = {}        
        scrape_dict['author'] = results[i][0]
        scrape_dict['created_utc'] = results[i][1]
        scrape_dict['id'] = results[i][2]
        scrape_dict['num_comments'] = results[i][3]
        scrape_dict['score'] = results[i][4]
        scrape_dict['title'] = results[i][5]
        scrape_dict['url'] = results[i][6]           
        interim_data.append(scrape_dict)
    return interim_data 


for x in range(0, 1500):
    y = x + 1
    days ='d'
    data = get_data("%s%s" % (y, days), "%s%s" % (x, days))
    final_data = final_data + (add_to_list(data))
    #time.sleep(1)

df_nottheonion = pd.DataFrame(final_data)
print(df_nottheonion.shape)

df_nottheonion.to_csv('worldnews_new.csv')
