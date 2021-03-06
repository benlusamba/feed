""" Extract File Generation """

import pandas as pd
import numpy as np
import urllib.request
import os
import csv
import requests
import json
import json as simplejson
import datetime
import os
import os.path
import datetime
from datetime import datetime
import time 

start = time.time()
# define parameters, including API KEY
params = (
    ('sources', 'the-new-york-times,the-washington-post,the-wall-street-journal,bbc-news,cnn'),
    ('apiKey', '68970^ahshifr'),
)

response = requests.get('https://newsapi.org/v2/top-headlines', params=params)

data = response.json()

print(response.text)
# write response as JSON file to enable parsing
f = open('./source/data.json', 'w')
simplejson.dump(data, f)
f.close()

#parse JSON file using pandas
data = pd.read_json('./source/data.json', lines=True)

df_json_raw = pd.read_json('./source/data.json')

# Add variables as desired e.g. 'source'
#df_json = df_json_raw.apply( lambda x: pd.Series([x[0]['title'],x[0]['description'],x[0]['publishedAt'],x[0]['source']]), axis = 1 )
#df_json = df_json_raw.apply( lambda x: pd.Series([x[0]['title'],x[0]['description']]), axis = 1 )

df_json = df_json_raw.apply( lambda x: pd.Series([x[2]['description'],x[2]['title']]), axis = 1)
datadf = pd.DataFrame(data['articles'])
print(datadf)
# Label columns for csv file
#df_json.columns=['Title','Description','Published At','Source']
df_json.columns=['Description', 'Title']

#export as csv, respect location and time conventions:
datestring = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')

archive = './archive'
df_json.to_csv(os.path.join(archive,r'newsfeed.txt'))
#path = 'C:/Users/BELUSA/Documents/Projects/alt/feed'
#df_json.to_csv(os.path.join(path,r'feed_'+datestring+'.csv'))


# Show file in workspace
print(data)
print (df_json)

print('')

print('Word Frequency Count')
import common

end = time.time()
print (f"Executed in {np.round(end-start)} seconds")