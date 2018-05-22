# Instances of speficic words in text
import re

feed = open('feed.csv')
for line in feed:
    line = line.rstrip()
    x = re.findall("Trump", line)
    y = re.findall("China", line)
    if len(x) > 0 and \
    len(y) > 0:
        print(x,y)
