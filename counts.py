"Using Regex to search for word count"
import re

#Input desired word
word = input('Targed Word: ')
count = 0
file = open('feed.csv')
for line in file:
    if re.search(word, line):
        count = count + 1
print (count)
