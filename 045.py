#!python
"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

from math import sqrt
from functools import lru_cache

@lru_cache(maxsize=None)
def is_pentagonal(n):
	x = (1+sqrt(1+24*n))/6
	y = (1-sqrt(1+24*n))/6
	return (x>0) and (x==int(x)) or (y>0)and(y==int(y))

@lru_cache(maxsize=None)
def is_triangular(n):
	x = (-1+sqrt(1+8*n))/2
	y = (-1-sqrt(1+8*n))/2
	return (x==int(x)) or (y==int(y))

def hexagonals(m=None):
	i = 1
	while True:
		p = int(i*(2*i-1))
		if (m is not None) and p > m:
		  return
		yield p 
		i+=1

if __name__=="__main__":
	print(list(filter(is_triangular, filter(is_pentagonal, hexagonals(10000000000)))))