#!python
"""
commonly used methods
"""

from math import factorial, sqrt
from fractions import gcd
from functools import reduce
from operator import mul

#misc
def product(l):
	return reduce(mul, l)


#combinatorics
def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield [elements[i]]
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield [elements[i]] + next

def choose(n, r):
	return int(factorial(n)/(factorial(r)*factorial(n-r)))


#ptyhagorean triples
def generate_primitive_triples(limit):
	for m in range(2,limit):
		for n in range(1,m):
			if(m-n)%2==1:
				if gcd(m,n)==1:
					a = m*m-n*n
					b = 2*m*n
					c = m*m+n*n
					if a > b:
						a, b = b, a
					if c < limit:
						yield [a, b, c]

#primes
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

def prime_factors(n):
	factors = []
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				factors.append(i)
				n = int(n/i)
				break
			i += 1
	return factors