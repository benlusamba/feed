#import pandas as pd
#import numpy as np
#import urllib.request, json, simplejson, csv, requests

#fname = input('Enter the file name: ')
#try:
fhand = open('feed.csv')
#except:
#    print('File cannot be opened:', fname)
#    exit()

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
