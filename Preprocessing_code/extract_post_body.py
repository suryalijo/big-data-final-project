from newspaper import Article
from newspaper import Config
import pandas as pd
#from urllib.request import Request, urlopen
from urllib.error import HTTPError

from http.client import IncompleteRead


df = pd.read_csv("worldnews_new_latest.csv", low_memory=False)

col_list_url = df['url'].tolist()

count = 0

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
#page = Article("https://www.newsweek.com/donald-trump-hillary-clinton-2020-rally-orlando-1444697", config=config)
#page.download()
#page.parse()
#print(page.text)

print(len(df))
body_text = []
keywo = []
for url in col_list_url:
        article = Article(url, config=config)
        article.download()
        try: 
            article.parse()
        except Exception as e:
            print(e)
            body_text.append('no text'+ str(e))
            keywo.append('no keyword')
        except HTTPError as e:
            print(e)
            body_text.append('no text' + str(e))
            keywo.append('no keyword')
        except IncompleteRead as e:
            print(e)
            body_text.append('no text' + str(e))
            keywo.append('no keyword')
            # Oh well, reconnect and keep trucking
            #continue
        else:
            body_text.append(article.text)
            keywo.append(article.keywords)
        count += 1
        print(count)

      
df['post body'] = body_text        
df['keywords'] = keywo

df.to_csv("worldnews_body_new.csv")
