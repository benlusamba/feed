#Regex Search Engine within file:
import re

stuff = input('What should I search for: ')

file = open('feed.csv')
for line in file:
    line = line.rstrip()
    if re.search(stuff, line):
        print(line)
