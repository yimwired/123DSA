#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from itertools import combinations

def is_alternating(s):
    return all(s[i] != s[i+1] for i in range(len(s) - 1))

def alternate(s):
    unique_chars = set(s)
    max_length = 0
    
    for char1, char2 in combinations(unique_chars, 2):
        filtered = [char for char in s if char in (char1, char2)]
        if is_alternating(filtered):
            max_length = max(max_length, len(filtered))
    
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input().strip()

    result = alternate(s)

    fptr.write(str(result) + '\n')
    fptr.close()
