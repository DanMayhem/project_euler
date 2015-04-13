#!python
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

from functools import lru_cache
from math import floor, sqrt, ceil


def prime_sieve(n):
	if n < 2:
		return
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

upper=100000
m=5
sieve = list(prime_sieve(10000000))
sieve_set = set(sieve)

def is_prime(n):
	return n in sieve_set

def is_addition_remarkable(x, s):
	"does adding x to a remarkable set s create a new remakrbale set?"
	xx = str(x)
	for p in s:
		if not is_prime(int(xx+str(p))):
			return False
		if not is_prime(int(str(p)+xx)):
			return False
	return True

@lru_cache(maxsize=None)
def produce_remarkable_sets_cached(s, n):
	return list(produce_remarkable_sets(s, n))

def produce_remarkable_sets(s, n):
	"enumerates every remarkable set of n primes that sum to s"
	if n==1:
		if is_prime(s):
			yield [s]
		return
	#ps = prime_sieve_cached(ceil(s/n))
	for p in sieve:
		if p*n > s:
			break
		for x in produce_remarkable_sets_cached(s-p, n-1):
			if is_addition_remarkable(p, x):
				yield x+[p]

if __name__=="__main__":
	for i in range(m*m,upper):
		for s in produce_remarkable_sets(i, m):
			print([sum(s), s])
			exit()

