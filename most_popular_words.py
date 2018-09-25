from collections import Counter
from nltk.corpus import stopwords

countdict={}
word_list=[]

for key in reviewText_3chr_rem_dict:
    word_list= word_list+reviewText_3chr_rem_dict[key].split(' ')
stop = stopwords.words('english') 
word_list_stop_rem=[i for i in word_list if i not in stop and i != ' ']
countdict=Counter(word_list_stop_rem).most_common(10)
rank = 0
for word, freq in countdict:
    rank += 1
    print("%d %s %d" % (rank,word,freq))