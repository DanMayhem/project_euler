#!python
"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
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

def phi_2(p, q):
	n = p*q
	pp = 1-(1/p)
	qp = 1-(1/q)
	return int(n*pp*qp)

def is_permutation(x, l):
	return str(sorted(list(str(x)))) == str(sorted(list(str(l))))

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
	primes = list(filter(partial(lt, 2000), prime_sieve(5000))) #primes between 2000 and 5000
	mf=999

	for p in primes:
		for q in primes:
			n  = p*q
			fn = phi_2(p, q)
			fr = n/fn
			if (fr < mf) and (n < 10**7):
				if is_permutation(n, fn):
					mf = fr
					print([n, fn, phi(n), fr])

	exit()

	for n in range(2,10**7):
		fn = phi(n)
		fr = n/fn
		if fr < mf:
			mf = fr
			if is_permutation(n, fn):
				print(n)

