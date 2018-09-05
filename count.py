#!/usr/bin/python 

import string
print("enter string: ") 
wordlist = raw_input() 

try:
    for letter in list(string.ascii_lowercase):
        if letter in wordlist.lower(): 
            amount = str(wordlist.lower().count(letter))
            print (letter + ":" + amount) 
except Exeption: 
    print "Unkown format error" 





""" initial failed try """
#def count_letters(word, char):
#    count = 0 
#    if c in word:
#        if char == c: 
#            count +=1
#    return count
# print count

