import requests
import json
import pandas as pd
from urllib.parse import unquote
from mymodules.mongodb import dataframe_to_mongo
from datetime import datetime,date,timedelta
import time

url = "https://api.twitter.com/1.1/trends/place.json?id=2487796"

payload = {}
headers = {
  'Authorization': 'OAuth oauth_consumer_key="UccGzWcgnIlMAvL3H7bZGmDrC",oauth_token="1142809701433917442-lpIm7w0cV6ow0dqGVYoD9kj8AFi6Ck",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1589338829",oauth_nonce="fWAg9ec89oL",oauth_version="1.0",oauth_signature="lY8jMsVhF6VWaEYq%2BAGEF%2Bgo2nE%3D"',
  'Cookie': 'personalization_id="v1_6stCa+fjoB4v2WpGChx+UQ=="; guest_id=v1%3A158932770384542900; lang=en'
}
def load_trends():
    response = requests.request("GET", url, headers=headers, data = payload)

    print(response)

    a_json = json.loads(response.text.encode('utf8'))

    trends = a_json[0]['trends']

    trends_df = pd.DataFrame(trends)

    trends_df_clean = trends_df[trends_df['tweet_volume'].notna()]

    trends_df_clean_select = trends_df_clean[['name','query','tweet_volume']]

    trends_df_clean_select['query'] = trends_df_clean_select['query'].apply(lambda x:unquote(x))

    trends_df_clean_select.sort_values(by=['tweet_volume'],ascending=False, inplace=True)

    dftomongo = trends_df_clean_select.head(10)

    current_timestamp = time.time()
    
    st = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')

    dataframe_to_mongo(dftomongo,"trend_bulk","trendcollection "+st)

