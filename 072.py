#!python
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

from operator import mul, lt
from functools import lru_cache, reduce, partial

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

def phi(n):
	return int(reduce(mul, map(lambda x: 1-1/x, distinct_prime_factors(n)))*n)

def phi_sieve(n):
	if n < 2:
		return
	s=[i for i in range(n)]
	for i in range(2,n):
		if s[i]==i:
			for j in range(i, n, i):
				s[j]=s[j] / i*(i-1)
	return s


if __name__=="__main__":
	max_d = 1000000
	print(sum(phi_sieve(max_d+1))-1)