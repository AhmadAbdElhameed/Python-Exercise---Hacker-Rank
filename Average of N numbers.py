# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:04:28 2021

@author: Ahmad Abd Elhameed
"""

num = int(input("How many numbers ?"))
total_sum = 0

for i in range(num):
    numbers = float(input("Enter any numbers"))
    total_sum += numbers

avg = total_sum / num
print("Average is :",avg)