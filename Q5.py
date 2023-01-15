# %% [markdown]
# ### Sentiment analysis. Develop a sentiment analysis tool for Starbucks stores. Pick any Starbucks location on Google Maps and access their reviews.

# %% [markdown]
# #### 5.1. [5 points] Steps for sentiment analysis: 

# %% [markdown]
# #### 5.1.1. Load the positive and negative words data3,4 using csv.reader into python. (Feel free to manually remove the header of the file)  

# %%
import csv

with open('negative-words.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('negative-words.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
        out_file.close()
    in_file.close()

# %%
import csv

with open('positive-words.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('positive-words.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)
        out_file.close()
    in_file.close()

# %% [markdown]
# #### 5.1.2. Write two functions (numPositiveWords, numNegativeWords) that take a text input and returns the total number of positive and negative words in that text. (You will need to go over the entire list of words in each file you loaded in the previous step) 

# %%
def numPositiveWords(lst):
    with open(lst) as f:
        flat_list=[word for line in f for word in line.split()]
    count = 0
    for i in range(len(flat_list)):
        with open('positive-words.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == flat_list[i]:
                    count += 1
    return count

# %%
mylst = open('mylst.txt', 'w')
mylst.write('my amazing sister has an amazing and accessible cat')
mylst.close()

numPositiveWords('mylst.txt')

# %%
def numNegativeWords(lst):
    with open(lst) as f:
        flat_list=[word for line in f for word in line.split()]
    count = 0
    for i in range(len(flat_list)):
        with open('negative-words.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == flat_list[i]:
                    count += 1
    return count

# %%
mylst = open('mylst.txt', 'w')
mylst.write('my abnormal sister has an abnormal and abusive cat')
mylst.close()

numNegativeWords('mylst.txt')

# %% [markdown]
# #### 5.1.3. Write a function that takes number of positive words, number of negative words, and total number of words in a string to return a sentiment score. Sentiment is calculated as: (“number of positive words” - “number of negative words”)/(total words). 

# %%
def calcSentiment(lst):
    with open(lst) as f:
        flat_list=[word for line in f for word in line.split()]
        total = len(flat_list)
        numposi = numPositiveWords('mylst.txt')
        numnega = numNegativeWords('mylst.txt')
        calcSentiment = (numposi - numnega) / total
    return calcSentiment

# %% [markdown]
# #### 5.1.4. Write a function that gets review string from a user and validates that the string is less than 280 characters. If the string is longer than 280 characters, print a warning message and truncate the review to 280 characters. 

# %%
def review():
    review = input('What do you think?')
    if len(review) > 280:
        print('Warning: Your review is too long!')
        review = review[:280]
        print("Your truncated message is: " + review)
        print(len(review))
    else:
        print("Thank you for reviewing!")
    return review

# %%
review()

# %% [markdown]
# #### 5.1.5. Print the number of positive words, negative words, and sentiment of the text.

# %%
rev = review()
mylst = open('mylst.txt', 'w')
mylst.write(rev)
mylst.close()
numposi = numPositiveWords('mylst.txt')
numnega = numNegativeWords('mylst.txt')
print('Positive:', numposi)
print('Negative:', numnega) 
sentiment = calcSentiment('mylst.txt')
print('Sentiment:', sentiment)

# %% [markdown]
# #### 5.1.6. If the sentiment is positive, print some happy message. If sentiment is negative, print a sad message. 

# %%
if sentiment > 0:
    print('Yay!')
else:
    print("Oh no!")


