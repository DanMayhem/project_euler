#!python
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from functools import partial
from operator import lt

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i


def is_permutation(a,b):
	return sorted(str(a))==sorted(str(b))

if __name__=="__main__":
	primes = list(filter(partial(lt,1000),prime_sieve(10000))) #primes between 1000 and 9999
	for i in range(len(primes)):
		for j in range(i+1,len(primes)):
			if is_permutation(primes[i],primes[j]):
				d = primes[j]-primes[i]
				if is_permutation(primes[i],primes[j]+d):
					if primes[j]+d in primes:
						print([primes[i],primes[j],primes[j]+d])
