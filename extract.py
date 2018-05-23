#Searching for Context

import re

file = open('feed.csv')
for line in file:
    line = line.rstrip()
    if re.search('Donald Trump', line):
        print(line)
