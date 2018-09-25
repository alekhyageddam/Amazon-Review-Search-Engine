# read the data
import json
with open('review.json') as json_file:  
    reviews = json.load(json_file)

reviewTextdict={}
content = " "
def print_reviews():
    for element in reviews:
        reviewerId = element['reviewerID']
        reviewText = element['reviewText'] 
        reviewTextdict[reviewerId]=element['reviewText']
        content = reviewerId + " " + reviewText
        print(content)
content = print_reviews()


