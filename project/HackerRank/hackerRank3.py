#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted = []
    k = k % 26  # Normalize k to avoid unnecessary rotations
    
    for char in s:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted.append(chr(shift + (ord(char) - shift + k) % 26))
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
