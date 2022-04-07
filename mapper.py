#!/usr/bin/env python3
  
# import sys because we need to read and write data to STDIN and STDOUT
import io
import sys

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
# reading entire line from STDIN (standard input)
for line in input_stream:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
      
    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print('{}\t1'.format(word.encode('utf-8')))