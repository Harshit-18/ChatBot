#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install nltk


# In[2]:


pip install newspaper


# In[3]:


from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text  import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[4]:


nltk.download('punkt', quiet=True)


# In[5]:


#get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text


# In[6]:


#print the article text
print(corpus)


# In[7]:


text = corpus
sentence_list = nltk.sent_tokenize(text)


# In[8]:


print(sentence_list)


# In[9]:


# Function to return the response to a random greeting
def greeting_response(text):
  text = text.lower()


  #Bots greeting response
  bot_greetings=['hey', 'howdy', 'hi', 'hellow', 'hola']
  #Users greeting
  user_greetings=['hi', 'hey', 'hellow', 'hola', 'geetings', 'wassup']

  for word in text.split():
    if word in user_greetings:
      return random.choice(bot_greetings)


# In[10]:


def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0,length))

  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp


  return list_index   


# In[11]:


#Create bots response
def bot_response(user_input):
  user_input =  user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_score = cosine_similarity(cm[-1],cm)
  similarity_score_list = similarity_score.flatten()
  index = index_sort(similarity_score_list)
  index = index[1:]
  response_flag = 0


  j = 0
  for i in range(len(index)):
    if similarity_score_list[index[i]] > 0.0:
      bot_response = bot_response+' '+sentence_list[index[i]]
      response_flag = 1
      j = j+1
    if j>2:
      break

    if response_flag == 0:
      bot_response = bot_response+' '+"I Apologise, i do not understand."


  sentence_list.remove(user_input)


  return bot_response   


# In[13]:


# Star The Chat
print('Doc Bot: I am a doc bot and i will answer your queries about chronic kidney diseases. If you want to exit press bye')

exit_list = ['exit', 'quit', 'bye', 'see you later', 'break']

while(True):
  user_input = input()
  if user_input.lower() in exit_list:
    print('Doc Bot: See you Soon again.....!')
    break
  else:
    if greeting_response(user_input)!= None:
      print('Doc Bot: '+greeting_response(user_input))
    else:
      print('Doc Bot: '+bot_response(user_input))


# In[ ]:




