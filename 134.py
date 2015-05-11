#!python
"""
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
"""

from pe import prime_sieve

def get_s(p1,p2):
	n=p2
	k = len(str(p1))
	while n%10**k!=p1:
		n=(n+p2)
	return n


limit = 1000004

primes = list(prime_sieve(limit))

s = 0
n = 0

for i in range(2,len(primes)-1):
	n = get_s(primes[i],primes[i+1])
	s+=n
	print([i,primes[i], n,s])

