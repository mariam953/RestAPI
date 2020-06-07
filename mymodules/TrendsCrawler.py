import requests
import json
import pandas as pd
from urllib.parse import unquote
from mymodules.mongodb import dataframe_to_mongo
from requests_oauthlib import OAuth1Session



twitter = OAuth1Session('UccGzWcgnIlMAvL3H7bZGmDrC',
                          client_secret='aJw3bZIOxr2I1jaHMsBAObCtiHDrsg2WVHVTI0CCUH0Mzxt8ka',
                          resource_owner_key='1142809701433917442-lpIm7w0cV6ow0dqGVYoD9kj8AFi6Ck',
                          resource_owner_secret='mJyvWtUI1BIYIdlr7cOyUxqhnTPdaSAALmRbkfgWrVgRC')

url = "https://api.twitter.com/1.1/trends/place.json?id=2487796"


def load_trends(created_at):
    response = twitter.get(url)

    print(response)

    a_json = json.loads(response.text.encode('utf8'))

    trends = a_json[0]['trends']

    trends_df = pd.DataFrame(trends)

    trends_df_clean = trends_df[trends_df['tweet_volume'].notna()]

    trends_df_clean_select = trends_df_clean[['name','query','tweet_volume']]

    trends_df_clean_select['query'] = trends_df_clean_select['query'].apply(lambda x:unquote(x))

    trends_df_clean_select.sort_values(by=['tweet_volume'],ascending=False, inplace=True)

    dftomongo = trends_df_clean_select.head(10)

    dataframe_to_mongo(dftomongo,"trend_bulk","trendcollection "+created_at)
    
    #print(trends_df_clean_select['query'].iloc[0])

    return trends_df_clean_select['query'].iloc[0]

