"Using Regex to search for word count"
import re
import csv

#Input desired word
word = input('Targed Word: ')
count = 0
file = open('feed.csv')
for line in file:
    if re.search(word, line):
        count = count + 1
print (count)

#Write Results to csv or txt file
result = str(count)
output = open('count' + '.csv','w') #export as .csv or .txt file
output.write('%s' % result)
output.close()