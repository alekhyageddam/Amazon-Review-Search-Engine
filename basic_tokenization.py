import re

def rm_punct(reviewTextdict):
    reviewText_punc_rem_dict={}
    for key in reviewTextdict:
        list_element=re.findall(r"\w+",reviewTextdict[key])
        str_element=' '.join(list_element).lower()
        reviewText_punc_rem_dict[key]=str_element
        print(str(key) + " " + str_element)
    return reviewText_punc_rem_dict
    
reviewText_punc_rem_dict=rm_punct(reviewTextdict)

#print(reviewText_punc_rem_dict)
def rm_less3_chr(reviewText_punc_rem_dict):
    reviewText_3chr_rem_dict={}
    for key in reviewText_punc_rem_dict:
        str_element=''
        split_list=reviewText_punc_rem_dict[key].split(' ')
        for i in split_list:
            if len(i)>=3:
                str_element= str_element+' ' + i
        reviewText_3chr_rem_dict[key]=str_element
        print(str(key) + str_element)
    return reviewText_3chr_rem_dict

rm_less3_chr(reviewText_punc_rem_dict)
reviewText_3chr_rem_dict = rm_less3_chr(rm_punct(reviewTextdict))

from nltk.stem.porter import PorterStemmer
#print(reviewText_3chr_rem_dict)
def nltk_stemmer():
    stemmer=PorterStemmer()
    reviewText_stem_dict={}
    for key in reviewText_3chr_rem_dict:
        split_list=reviewText_3chr_rem_dict[key].split(' ')
        stemmed_list=[stemmer.stem(plural) for plural in split_list]
        str_element=' '.join(stemmed_list)
        reviewText_stem_dict[key]=str_element
        print(str(key) + str_element)
    return reviewText_stem_dict
output = nltk_stemmer()