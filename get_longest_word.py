"""
Problem Statement:
Implement a function longestWord() that takes a list of words and returns the longest one.
"""

from functools import reduce
list_words = ["This","is","a","beautiful","morning"]

# Function to compare and reduce list to the result
def longestWord(list_words):
 return reduce( (lambda x,y:y if len(y) > len(x) else x), list_words )

print ('Longest word in array ["This","is","a","beautiful","morning"] => ' + longestWord(list_words) )

