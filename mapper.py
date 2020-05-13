#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import stop_words

stops = set(stop_words.ENGLISH_STOP_WORDS)
stops.update('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') # add digits to stopwords (brute force way)
stops.update(['thou', 'shall', 'thee']) # notice, update needs a formal "set", or else it will add each single character...

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace and convert to lowercase
    line = line.strip().lower()

    # remove punctuation
    # (I wonder if it would be best done on the full line here, vs. on 'words' after the split)?
    line = line.translate(string.maketrans("",""), string.punctuation)
    
    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format, but only if they're not a stopword!
    for word in words:
        if word not in stops: # omit stopwords
            if len(word) > 3: # ignore words shorter than 3 characters
                print '%s\t%s' % (word, "1")
