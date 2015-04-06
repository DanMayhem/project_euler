#!python
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

from operator import add
from functools import reduce

if __name__=="__main__":
	print(reduce(add,map(int,list(str(2**1000)))))