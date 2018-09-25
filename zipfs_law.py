'''The Zipf function as defined in the textbook is:log cfi = log c - log i.
   Frequency is plotted as a function of frequency rank for the terms in the collection.
'''
import re
from operator import itemgetter
import matplotlib.pyplot as plt
from scipy import special
import numpy as np

#open file, convert to a string
open_file = open('review.json','r')
file_to_string = open_file.read()

#define a frequency dictionary
frequency = {}

#find all the words that begin with a upper or lowercase letter
words = re.findall(r'(\b[A-Za-z][a-z]{2,9}\b)', file_to_string)

#calculate the frequency of each word
for word in words:
    count = frequency.get(word,0)
    frequency[word] = count + 1

#store the frequency values(counts) in an number array 's'
frequency = {key:value for key,value in frequency.items()}
s = frequency.values()
s = np.array(s)

#Calculate zipf and plot the data
a = 2. #distribution parameter
plt.title("Zipf plot for Amazon Reviews")
x = np.arange(1.,15.) #len(frequency.values()
plt.xlabel("log10 rank")
y = x**(-a) / special.zetac(a)
plt.ylabel("log10 cf")
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()