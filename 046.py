#!python
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from math import floor, sqrt

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

def is_twice_square(n):
	for i in range(1,n):
		if n == 2*i*i:
			return True
	return False

if __name__=="__main__":
	m = 100000
	primes = set(prime_sieve(m))
	composites = set(range(9,m,2)) - primes

	primes = list(primes)
	primes.sort()

	for c in sorted(list(composites)):
		g = False
		for p in primes:
			if p > c:
				break
			if is_twice_square(c-p):
				g = True
				break
		if not g:
			print(c)

