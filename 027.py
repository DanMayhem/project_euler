#!python
"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from math import sqrt, floor

def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))):
		if n%i==0:
			return False
	return True

def resolve_quad(a,b,n):
	return n*n+a*n+b

def quadratic_prime_generator(a, b):
	i=0
	q = resolve_quad(a,b,i)
	while is_prime(q):
		yield q
		i+=1
		q = resolve_quad(a,b,i)

if __name__=="__main__":
	l=0
	p=0
	for a in range(-1000,1001):
		for b in range(-1000,1001):
			x = len(list(quadratic_prime_generator(a,b)))
			if x > l:
				l=x
				p=a*b
	print(p)
