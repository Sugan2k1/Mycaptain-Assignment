#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:16:43 2021

@author: sugan
"""

def Fibonacci(n):
   
    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
print(Fibonacci(11))
