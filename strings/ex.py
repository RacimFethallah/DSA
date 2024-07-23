#!/bin/python3

import math
import os
import random
import re
import sys


import string
#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    words = sentence.split(" ")
    
    
    new_sentence = ''
    for word in words:
        for i in range(len(word)):
            if word[i] == 0:
                new_sentence += word[i]
                continue
            if word[i] > word[i - 1]:
                new_sentence += word[i].upper()
            elif word[i] < word[i - 1]:
                new_sentence += word[i].lower()
            else:
                new_sentence += word[i]
        new_sentence += " "
                
            
    return new_sentence
            
            
            
            
            
            
            

if __name__ == '__main__':
    sentence = "a Blue MOON"

    result = transformSentence(sentence)
    print(result)
