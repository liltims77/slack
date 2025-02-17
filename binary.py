#!/bin/python3

import math
import os
import random
import re
import sys

n = 13

def max_consecutive_ones(n):
    # Convert to binary and remove the '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Split by '0' to find sequences of consecutive '1's
    ones_groups = binary_representation.split('0')
    
    # Find the length of the longest group of '1's
    max_ones = max(len(group) for group in ones_groups)
    
    return max_ones

if __name__ == '__main__':
    # n = int(input().strip())
    result = max_consecutive_ones(n)
    print(result)
