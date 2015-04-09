#!python
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from functools import lru_cache
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

def is_pandigital(x):
	s = list(str(x))
	s.sort()
	for i in range(len(s)):
		if str(i+1) != s[i]:
			return False
	return True

def _find_k(a):
	k=-1
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			k = i
	return k

def _find_l(a, k):
	l = -1
	for i in range(k+1,len(a)):
		if a[k] > a[i]:
			l=i
	return l


def gen_pandigital_n_desc(n):
	a = list(reversed([i+1 for i in range(n)]))
	yield int(''.join(map(str,a)))
	k=0
	while k>-1:
		k = _find_k(a)
		l = _find_l(a, k)
		x = a[k]
		a[k] = a[l]
		a[l] = x
		a[k+1:] = reversed(a[k+1:])
		yield int(''.join(map(str,a)))


if __name__=="__main__":
	for r in range(9,0,-1):
		for p in gen_pandigital_n_desc(r):
			if is_prime(p):
				print(p)
				exit()