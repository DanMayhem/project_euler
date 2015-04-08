#!python
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from functools import lru_cache
from math import floor, sqrt

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

@lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

def _is_ltrunc(n):
	if n >= 10:
		if not _is_ltrunc(int(str(n)[1:])):
			return False
	return is_prime(n)

def _is_rtrunc(n):
	if n >= 10:
		if not _is_rtrunc(int(str(n)[:-1])):
			return False
	return is_prime(n)

def _is_trunc(n):
	return _is_ltrunc(n) and _is_rtrunc(n)
	if n >= 10:
		if not _is_trunc(int(str(n)[1:])):
			return False
		if not _is_trunc(int(str(n)[:-1])):
			return False
	return is_prime(n)

def truncatable_primes(max):
	for p in prime_sieve(max):
		if p > 7:
			if _is_trunc(p):
				yield p

if __name__=="__main__":
	l = list(truncatable_primes(1000000))
	print(l)
	print(len(l))
	print(sum(l))