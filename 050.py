#!python
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from math import sqrt, floor
from functools import lru_cache

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

def flcsil(l):
	ll = set(l)
	m = max(l)
	for i in range(len(l),2,-1): #for every possible length of a sub array
		s = sum(l[0:i])
		for j in range(len(l)-i-1): #for each sub array
			if s > m:
				break
			if  (s in ll):
				return l[j:j+i]
			s += l[j+i]-l[j]
	return []

if __name__=="__main__":
	m = 1000000
	ps = prime_sieve(m)
	l = flcsil(list(ps))
	print(l)
	print(sum(l))
