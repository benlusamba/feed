"Using Regex to search for word count"
import re
import csv
import string

#Input desired word
word = input('Targed Word: ')
count = 0
file = open('feed.csv')
for line in file:
    if re.search(word, line):
        count = count + 1
print ("Word Count:", count)

count = 0
file = open('feed.csv')
upper_word = string.capwords(word)
for line in file:
    if re.search(upper_word, line):
        count = count + 1
print ("Word Count:", count)

count = 0
file = open('feed.csv')
capital_word = word.upper()
for line in file:
    if re.search(capital_word, line):
        count = count + 1
print ("Word Count:", count)

#Write Results to csv or txt file
result = str(count)
output = open('count' + '.csv','w') #export as .csv or .txt file
output.write('%s' % result)
output.close()
