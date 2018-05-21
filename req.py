# Automated news retrieval using newsapi.org (or other API of your choosing)
# Obviating need for a "curl" request

import pandas as pd
import numpy as np
import urllib.request, json, simplejson, csv, requests


# define parameters, including API KEY
params = (
    ('sources', 'the-new-york-times,the-washington-post,the-wall-street-journal,bbc-news,cnn'),
    ('apiKey', 'e76a07388cad49b49075abced2862f3d'),
)

response = requests.get('https://newsapi.org/v2/top-headlines', params=params)

data = response.json()

# write response as JSON file to enable parsing
f = open('data.json', 'w')
simplejson.dump(data, f)
f.close()

#parse JSON file using pandas
data = pd.read_json('data.json', lines=True)

df_json_raw = pd.read_json('data.json')

# Add variables as desired e.g. 'source'
df_json = df_json_raw.apply( lambda x: pd.Series([x[0]['title'],x[0]['description'],x[0]['publishedAt'],x[0]['source']]), axis = 1 )

 # Label columns for csv file
df_json.columns=['Title','Description','Published At','Source']

#export as csv
df_json.to_csv('feed.csv')

# Show file in workspace
print(data)
print(df_json)

fhand = open('feed.csv')

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])
