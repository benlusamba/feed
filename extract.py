# fixing needed
#Searching for Context

import re

file = open('feed.csv')
for line in file:
    line = line.rstrip()
    if re.search('Trump', line):
        print(line)
