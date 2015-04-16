#!python
"""
commonly used methods
"""

from math import factorial

def choose(n, r):
	return int(factorial(n)/(factorial(r)*factorial(n-r)))



