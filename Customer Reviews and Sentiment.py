# %%
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import nltk
from nltk.tokenize import WordPunctTokenizer
from yelpapi import YelpAPI
from pprint import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# %%
# retrieve API key
api_key = 'KvcndsGzfOBtdy9XgfZft8gfjUcwGQVX1TgfaZSmG0GzAX6r8S3dJb_X6Hy92gvWRZr7TMgEyZMRuvvLBd_TRSXceSBxqTS_ej8sjT-osTezJ1-jkrr1k7MTNquPY3Yx'

# %%
# use api key and search for various starbucks locations and three competitors
yelp_api = YelpAPI(api_key)
starbucks = yelp_api.search_query(term='starbucks', location='atlanta, ga', sort_by='rating', limit=5)
dunkin = yelp_api.search_query(term='dunkin', location='atlanta, ga', sort_by='rating', limit=3)
costa = yelp_api.search_query(term='costa cofee', location='atlanta, ga', sort_by='rating', limit=3)
kaldi = yelp_api.search_query(term='Kaldi', location='atlanta, ga', sort_by='rating', limit=3)

# %%
# initalize dictionaries to store the reviews for each store
review_s1 = yelp_api.reviews_query(id="Rw_YSIKnkYii5WIeAynaSw", limit=10)
review_s2 = yelp_api.reviews_query(id="jvsSOoU5XGAX948CRhNELg", limit=10)
review_s3 = yelp_api.reviews_query(id="VgUeFkIliOQEmHlIFli9gg", limit=10)
review_dk = yelp_api.reviews_query(id="4upVxMjwp32xbEBBULewoQ", limit=10)
review_cos = yelp_api.reviews_query(id="y6i9mMxf6X7Jn-UA74Lc6A", limit=10)
review_kal = yelp_api.reviews_query(id="eMyl3yZ4_NEVo9huLcEdoA", limit=10)

# %%
# Use SentimentIntensity Analyzer to get polarity scores of each set of reviews
sid = SentimentIntensityAnalyzer() 

# initialize a list for positive and negative scores
s1_neg = []
s1_pos = []
s1_review_list = []

# iterate each review and append to empty list above
for i in range(0, 3):
    s1_review_list.append(review_s1["reviews"][i]["text"])
    
# loop through each review, store positive and negative sentiment scores for each review and print the sentimental score
for review in s1_review_list:
    sentiment_s1 = sid.polarity_scores(review)
    print("Sentiment scores for yelp reviews in the first Starbucks location: ", sentiment_s1)
    s1_neg.append(sentiment_s1['neg'])
    s1_pos.append(sentiment_s1['pos'])

# %%
# Second Starbucks Location
s2_neg = []
s2_pos = []
s2_review_list = []

for i in range(0, 3):
    s2_review_list.append(review_s2["reviews"][i]["text"])
    
for review in s2_review_list:
    sentiment_s2 = sid.polarity_scores(review)
    print("Sentiment scores for yelp reviews in the second Starbucks location: ", sentiment_s2)
    s2_neg.append(sentiment_s2['neg'])
    s2_pos.append(sentiment_s2['pos'])

# %%
# Third Starbucks Location
s3_neg = []
s3_pos = []
s3_review_list = []

for i in range(0, 3):
    s3_review_list.append(review_s3["reviews"][i]["text"])
    
for review in s3_review_list:
    sentiment_s3 = sid.polarity_scores(review)
    print("Sentiment scores for yelp reviews in the third Starbucks location:: ", sentiment_s3)
    s3_neg.append(sentiment_s3['neg'])
    s3_pos.append(sentiment_s3['pos'])

# %%
# Dunkin Reviews

dk_neg = []
dk_pos = []
dk_review_list = []

for i in range(0, 3):
    dk_review_list.append(review_dk["reviews"][i]["text"])
    
for review in dk_review_list:
    sentiment_dk = sid.polarity_scores(review)
    print("Sentiment scores for yelp reviews of Dunkin: ", sentiment_dk)
    dk_neg.append(sentiment_dk['neg'])
    dk_pos.append(sentiment_dk['pos'])

# %%
# Costa Reviews
cos_neg = []
cos_pos = []
cos_review_list = []

for i in range(0, 3):
    cos_review_list.append(review_cos["reviews"][i]["text"])
    
for review in cos_review_list:
    sentiment_cos = sid.polarity_scores(review)
    print("Sentiment scores for yelp reviews of Costa: ", sentiment_cos)
    cos_neg.append(sentiment_cos['neg'])
    cos_pos.append(sentiment_cos['pos'])

# %%
# Kaldi Reviews

kal_neg = []
kal_pos = []
kal_review_list = []

for i in range(0, 3):
    kal_review_list.append(review_kal["reviews"][i]["text"])
    
for review in kal_review_list:
    sentiment_kal = sid.polarity_scores(review)
    print("Sentiment scores for reviews of Kaldi: ", sentiment_kal)
    kal_neg.append(sentiment_kal['neg'])
    kal_pos.append(sentiment_kal['pos'])

# %%
# sort through positive and negative words and store them separately to create the wordclouds for Starbucks

# initalize lists for positive and negative reviews
sb_pos = []
sb_neg = []

# if the sentiment score is higher for positive than negative, append the review onto the list of positive reviews
# else, append the review onto the list of negative reviews

# First Starbucks Location
for i in range(0,3):
    if s1_pos[i] > s1_neg[i]:
        sb_pos.append(review_s1["reviews"][i]["text"])
    else:
        sb_neg.append(review_s1["reviews"][i]["text"])

# Second Starbucks Location
for i in range(0,3):
    if s2_pos[i] > s2_neg[i]:
        sb_pos.append(review_s2["reviews"][i]["text"])
    else:
        sb_neg.append(review_s2["reviews"][i]["text"])
        
# Third Starbucks Location
for i in range(0,3):
    if s3_pos[i] > s3_neg[i]:
        sb_pos.append(review_s3["reviews"][i]["text"])
    else:
        sb_neg.append(review_s3["reviews"][i]["text"])

# %%
# Create a wordcloud for Starbucks reviews that are more positive

sb_pos = ''.join(sb_pos)        
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(sb_pos)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# %%
# Negative Reviews Wordcloud for Starbucks

sb_neg = ''.join(sb_neg)        
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(sb_neg)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# %%
# combine the positive and negative reviews for the 3 competitions into separate lists

comp_pos = []
comp_neg = []

# Dunkin Reviews
for i in range(0,3):
    if dk_pos[i] > dk_neg[i]:
        comp_pos.append(review_dk["reviews"][i]["text"])
    else:
        comp_neg.append(review_dk["reviews"][i]["text"])

# Costa Reviews
for i in range(0,3):
    if cos_pos[i] > cos_neg[i]:
        comp_pos.append(review_cos["reviews"][i]["text"])
    else:
        comp_neg.append(review_cos["reviews"][i]["text"])

# Kaldis Reviews
for i in range(0,3):
    if kal_pos[i] > kal_neg[i]:
        comp_pos.append(review_kal["reviews"][i]["text"])
    else:
        comp_neg.append(review_kal["reviews"][i]["text"])

# %%
# WordCloud for the positive reviews for the competition

comp_pos = ''.join(comp_pos)        
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(comp_pos)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# %%
# WordCloud for the negative reviews for the competition

comp_neg = ''.join(comp_neg)        
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(comp_neg)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()



