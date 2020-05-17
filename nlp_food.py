#NLP food
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from collections import Counter

#importing the dataset
dataset = pd.read_csv('exported_data/full_gpa.csv')
comfort_food = dataset[['comfort_food', 'GPA']]
comfort_food = comfort_food[comfort_food['comfort_food'].notna()].reset_index(inplace = False)
comfort_food.drop('index', axis='columns', inplace=True)
#comfort_food.insert(0, 'New_ID', range(1000, 1000 + len(comfort_food))) - for unique ID


#cleaning the text
#first step: keep only letters. punctuation and numbers will be removed
response = re.sub('[^a-zA-Z]',' ', comfort_food['comfort_food'][0])
#[^a-z] 0 means we don't want to remove any letters a-z, whether it's capital or not.
#sub is to replace substrings. the first parameter is for what you want to replace
#the second is what should replace the 1st, and the last one is where.
#we add ' ' not to mix different words
response = response.lower()

#initialize the new lis of dataset
corpus = [] #corpus is a collection of text
for i in range(120):
    response = re.sub('[^a-zA-Z]', ' ', comfort_food['comfort_food'][i])
    response = response.lower()
    response = response.split()
    ps = PorterStemmer()
    response = [ps.stem(word) for word in response if not word in 
              stopwords.words('english')]
    response = ' '.join(response)
    corpus.append(response)


#creating a text file with all words
full_comfort_food  = []
       
def listToString(s):  
    str1 = " " 
    return (str1.join(s))

full_comfort_food = listToString(corpus)


#count frequent words
split_it = full_comfort_food.split() 
Counter = Counter(split_it) 
most_occur = Counter.most_common(20)  








