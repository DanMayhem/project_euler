#!python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

def lcm(a, b):
	x = max([a,b])
	for i in range(x, a*b):
		if (i%a==0) and (i%b==0):
			return i
	return a*b

if __name__ == '__main__':
	print(reduce(lcm, range(1,21)))