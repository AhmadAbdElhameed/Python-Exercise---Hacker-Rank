# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:05:36 2021

@author: Ahmad Abd Elhameed
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    result = []
    for i in range(1,n+1):
        if ((i%3 == 0) & (i%5 == 0)):
            result.append("FizzBuzz")
        elif ((i%3 == 0) & (i % 5 != 0)) :
            result.append("Fizz")
        elif ((i%3 != 0) & (i % 5 == 0)):
            result.append("Buzz")
        else :
            result.append(str(i))
    return result
        
            
def main():
    print('\n'.join(fizzBuzz(15)))

main()

