import math
import sys
from collections import defaultdict
import numpy as np
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

dictionary = set()

for key in reviewText_3chr_rem_dict:
    list_words = reviewText_3chr_rem_dict[key].split(" ")
    dictionary=dictionary.union(set(list_words))

global N
N = len(reviewText_3chr_rem_dict)

postings={}    
for word in dictionary:
    postings[word]=0
    for key in reviewText_3chr_rem_dict:
        if word in reviewText_3chr_rem_dict[key].split(" "):
            postings[word]= postings[word]+1

TF_dict={}    
for key in reviewText_3chr_rem_dict:
    list_words = reviewText_3chr_rem_dict[key].split(" ")
    tf_list=[]
    for i in dictionary:
        try:
            tf_list=tf_list+[float(1+math.log(list_words.count(i),10))]
        except:
            tf_list=tf_list+[float(list_words.count(i))]
    TF_dict[key] = tf_list
    
def idf(term,postings):
    if term in dictionary:
        return math.log(N/postings[term],10)
    else:
        return 0.0
        
IDF_list=[]
for word in dictionary:
    IDF_list=IDF_list+[idf(word,postings)]

TFIDF_dict={}
for key in TF_dict:
    TFIDF_dict[key]=[a*b for a,b in zip(TF_dict[key],IDF_list)]  
    
def calc_query_score(query):
    query_tf_list=[]
    for i in dictionary:
        query_tf_list=query_tf_list+[float(query.split(" ").count(i))]
    
    score_dict={}    
    for key in TF_dict:
        #score_dict[key]=sum([a*b for a,b in zip(TFIDF_dict[key],query_tf_list)])
        score_dict[key] = dot(TFIDF_dict[key],query_tf_list)/norm(TFIDF_dict[key])/norm(query_tf_list)
    score_sorted_keys = sorted(score_dict, key=score_dict.get, reverse=True)
    rank = 0
    for r in score_sorted_keys[:10]:
        rank = rank + 1
        print(rank, r, score_dict[r])   
    return(score_dict)   

