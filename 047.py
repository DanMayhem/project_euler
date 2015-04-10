#!python
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from functools import partial, reduce, lru_cache
from operator import __and__, eq, add

def prime_factors(n):
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				yield i
				n = int(n/i)
				break
			i += 1

@lru_cache(maxsize=16)
def num_distinct_factors(n):
	return len(set(prime_factors(n)))

def is_interesting(x,n):
	for i in range(n):
		if num_distinct_factors(x+i)!=n:
			return False
	return True

if __name__=="__main__":
	n = 4
	for i in range(2,1000000):
		if is_interesting(i,n):
			for j in range(n):
				print(i+j)
			exit()

