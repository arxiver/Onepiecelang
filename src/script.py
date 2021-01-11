#!/usr/bin/env python
# coding: utf-8

# """  
# ### Title: M.I. assignment problem no. 1  
# ### Author: Mohamed Mokhtar Abdelrazek  
# ### Section: 2  
# ### B.N.: 17  
# """  

# In[1]:


import time
import numpy as np
import re


# In[2]:


def read_unigrams(path):
    """
    Reading the words dataset and store it into a dictionary
    and setting weight for each word using log of (words_count - word_order)
    higher order, better weight.
    Args:
        path: string of the path of the file.
    Returns:
        words: dict of the words and each with a given weight.
        max_len: maximum length of words in the dict.
    """
    words = {}
    max_len = 0
    file = open(path).read().split()
    words_count = len(file)
    words = {}
    for (i,word) in enumerate(file):
        words[word] = np.log(i+1)
        if (len(word) > max_len):
            max_len = len(word)
    return words, max_len


# In[3]:


def find_spaces(sentence, unigrams, window_size):
    """
    Args:
        sentence: string the sentence/url before processing (concatenated sentence)
        unigrams: dict the words in the data-set with corresponding weight
        window_size: maximum word length in the dict
    Returns:
        separated: list of strings words after separation 
    """
    # s_lower: string holds the lowercase of the sentence because the dict is built on lowercase words
    sentence = clean_sentence(sentence)
    sentence = sentence.replace(' ','')
    s_lower = sentence.lower()
    weights = [0]
    splits = []
    separated = []
    # i represnts the end of the sentence which i will look before
    # For every letter from [i=1 to len(s)+1] and try to split each word at each letter
    for i in range(1, len(s_lower)+1):
        w_min, w_count = minimize_sentence_cost(s_lower, unigrams, i, weights, window_size)
        weights.append(w_min)
        splits.append(w_count)

    i = len(sentence)
    while i > 0:
        j = splits[i-1]
        separated.append(sentence[i-j:i])
        i -= j
        
    separated = list(reversed(separated))
    return separated


# In[4]:


def minimize_sentence_cost(sentence, unigrams, i, weights, window_size):
    """
    Minimize the sentence cost at the current index by looking backwards and trying to find best word 
    can minimize the cost of the sentence 
    e.g. sentence: He is good, and my ptr is standing at 's'
    It will try to split all previous letters in window of size 
    Args:
        sentence: string the sentence concatenated without spaces.
        unigrams: dict each word as key in the data-set and its cost as value.
        i: int the end of the ptr of current processign word.
        weights: list the cost of the sentence at each index with respect to each split.
        window_size: int maximum word length in the unigrams.
    Returns:
        cost_min: float the new cost of the sentence with respsect to 'i' letter's split happend.
        cost_min_j: int the count of letters taken with backwards from 'i' to make this minmum cost.
    """
    # i is the end of the ptr of current processing word
    # We look before it letter by letter and split the subword incrementally,
    # and trying to find subword which minimize cost of sentence, 
    # and cost of splitting this word in addition of to the cost of sentence
    start = max(0, i-window_size)
    prefix_costs = weights[start:i]
    cost_min, letters_count = 1000, 0
    """
    Minimize [cost(left_sub_word) + cost(right_sub_word)]
    Minmum cost of sentence when took this split cost(left) + cost(right)
    W_j: W_0j (sub-word from letter 0 to letter j), 
         Cost of the prefix word from current_letter-j-max_word_length to current_letter-j
    W_ji = W_ji (sub-word from letter j to letter i-1)
    Update new minimum cost
    """
    for j in range(len(prefix_costs)):
        # Weight of sub_word at previous of i [-ive] access e.g. j=0 
        # e.g. preifixs[-1] means i take letter at i-1 as a letter only and rest of word's cost
        w_j =  prefix_costs[-(j+1)] 
        # Weight of sub_word j->i
        w_ji = unigrams.get(sentence[i-j-1:i]) 
        # If there is a matching word that preceeds i with j_letters_count 
        # And cost of (word_0j + word_ji) < cost_of_min_split_happend_before
        # Update cost
        if w_ji != None and cost_min > (w_j + w_ji):
            # Update new cost
            cost_min = w_j + w_ji
            # length of prefix letters included with letter i to make minmium cost of sentence
            letters_count = j+1
    return cost_min, letters_count


# In[5]:


def clean_sentence(s):
    # remove anything except a..z and A..Z and space and dots.
    return re.sub("[^a-zA-Z .]","",s)


# In[6]:


def score(X, Y, unigrams, max_len):
    """
    Args:
        X: list of sentences 
        Y: list of lists, for each sentence its corresponding actual output separated list.
        unigrams: dictionary the words in the data-set with corresponding weight
        window_size: maximum word length in the dictionary

    Returns:
        score: number of correctly separated words in exact place corresponding 
        to same place and value in the actual output list 
        divided by the total number of tested words, and multiplied by 100
    """
    total_words = 0
    correct = 0
    correct_sentences = 0
    for i in range(len(X)):
        total_words += len(Y[i])
        y_hat = find_spaces(X[i],unigrams, max_len)
        ptr_hat = 0
        ptr_tmp = 0
        for word in Y[i]:
            if ptr_hat >= len(y_hat):
                break
            elif(word == y_hat[ptr_hat]):
                correct +=1
                ptr_hat +=1
            else:
                ptr_tmp = ptr_hat
                while (ptr_tmp < len(y_hat) and y_hat[ptr_tmp] != word):
                    ptr_tmp +=1 
                if (ptr_tmp != len(y_hat)):
                    ptr_hat = ptr_tmp + 1
                    correct +=1
        if(ptr_hat == len(Y[i])):
            correct_sentences +=1
    print("No. of sentences:", len(X))
    print("No. of total words:", total_words)
    print("No. of correct words:", correct)
    print("No. of completely correct sentences:", correct_sentences)
    return float("{:.2f}".format((correct/total_words) * 100))


# In[7]:


def read_testset(path):
    """
    Reading the words dataset and store it into a dictionary
    and setting weight for each word using log of (words_count - word_order)
    higher order, better weight.
    Args:
        path: string of the path of the file.
    Returns:
        words: dict of the words and each with a given weight.
        max_len: maximum length of words in the dict.
    """
    X = []
    Y = []
    with open(path) as f:
        for s in f:
            s = clean_sentence(s)
            s = s.replace('.','')
            X.append(s.replace(' ',''))
            Y.append(s.split(' '))
    return X,Y


# In[8]:

if __name__ == '__main__':

    # read the dictionary
    unigrams,max_length = read_unigrams("../data/unigrams.txt")
    s = "welcometomyworld" #replace this with your sentence or if you want to use it as input just uncommenct next line
    s = input("Enter your sentence: ")
    print(find_spaces(s,unigrams, max_length))


