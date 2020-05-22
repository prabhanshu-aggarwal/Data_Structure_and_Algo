# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:27:49 2020

@author: Prabhanshu Aggarwal
"""

#Create a function called word_split() which takes in a string phrase and a set list_of_words

#word_split('themanran',['the','ran','man']) ==>  ['the', 'man', 'ran']
#word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']) ==>  ['i', 'love', 'dogs', 'John']

def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []
        
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word): ], list_of_words, output)
    return output   
            