#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Reverse the string
    reversed_s = s[::-1]
    
    # Calculate the absolute differences for the original string
    original_diffs = [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)]
    
    # Calculate the absolute differences for the reversed string
    reversed_diffs = [abs(ord(reversed_s[i]) - ord(reversed_s[i+1])) for i in range(len(reversed_s)-1)]
    
    # Compare the two lists of differences
    if original_diffs == reversed_diffs:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
