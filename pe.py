#!python
"""
commonly used methods
"""

from math import factorial, sqrt, floor
from fractions import gcd
from functools import reduce
from operator import mul
from itertools import combinations

#misc
def product(l):
	return reduce(mul, l, initializer=1)


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

def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

def rad(n):
	if n == 1:
		return 1
	return product(set(prime_factors(n)))

#fibonacci
def fib(max=None):
	a = 0
	b = 1
	while (max is None) or (b < max):
		yield b
		c = a + b
		a = b
		b = c

#pandigital numbers
def is_pandigital(x):
	s = list(str(x))
	s.sort()
	for i in range(len(s)):
		if str(i+1) != s[i]:
			return False
	return True

#"special" sets

def is_special_pair(b, c):
	def s(a):
		return sum(a)
	if len(b) == len(c):
		return s(b) != s(c)
	if len(b) < len(c):
		b, c = c, b
	if s(b) <= s(c):
		return False
	return True

def is_special_set(a):
	for i in range(1,len(a)//2+1):
		for b in combinations(a, i):
			b = set(b)
			x = a-b
			for j in range(1,len(x)+1):
				for c in combinations(x, j):
					if not(is_special_pair(b, c)):
						return False
	return True

#palindromes
def is_palindrome(i):
	return i == int(str(i)[::-1])
