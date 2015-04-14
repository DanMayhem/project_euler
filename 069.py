#!python
"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from functools import lru_cache, reduce
from operator import mul

def prime_factors(n):
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				yield i
				n = int(n/i)
				break
			i += 1

@lru_cache(maxsize=None)
def distinct_prime_factors(n):
	return set(prime_factors(n))

def phia(n):
	factors = distinct_prime_factors(n)
	def _is_rel_prime(b):
		return len(factors & distinct_prime_factors(b))==0
	return len(list(filter(_is_rel_prime, range(1,n))))

def phi(n):
	return int(reduce(mul, map(lambda x: 1-1/x, distinct_prime_factors(n)))*n)


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


if __name__=="__main__":
	p = 1
	for n in prime_sieve(100000):
		p*=n
		if p > 1000000:
			print(int(p/n))
			exit()