#Searching for Context

import re

hand = open('feed.csv')
for line in hand:
    line = line.rstrip()
    if re.search('Donald Trump', line):
        print(line)
