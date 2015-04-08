#!python
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from functools import partial, lru_cache
from operator import mod
from math import ceil, sqrt

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

def primes(n):
	p=[]
	def _has_factor(x):
		return 0 in map(partial(mod, x), p)
	for i in range(2,n):
		if not _has_factor(i):
			p.append(i)
			yield i

@lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2,ceil(sqrt(n))):
		if n%i==0:
			return False
	return True

def cycles(n):
	s = str(n)
	for i in range(len(s)):
		yield int(s[i:]+s[:i])

def circular_primes(n):
	for p in prime_sieve(n):
		if False not in map(is_prime,cycles(p)):
			yield p

if __name__=="__main__":
	l = list(circular_primes(1000000))
	print(l)
	print(len(l))
