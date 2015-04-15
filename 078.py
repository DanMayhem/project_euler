#!python
"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""

from math import factorial
from functools import lru_cache

def choose(n, r):
	return int(factorial(n)/(factorial(r)*factorial(n-r)))

@lru_cache(maxsize=4096)
def n_terms_sum_to_a_count(a, n, m):
	#print([a, n, m])
	if n==1:
		if a <= m and a>0:
			return 1
		return 0
	collection = 0
	for i in range(1,min([a, m+1])):
		#print([a,n,i])
		collection+= n_terms_sum_to_a_count(a-i, n-1, min([m, i]))
	return collection

def old_p(n):
	c=0
	for i in range(1,n+1):
		c+= n_terms_sum_to_a_count(n,i,n)
	return c


def nth_pentagonal(n):
	return int(n*(3*n-1)/2)

def gen_gen_pentagonal(n):
	#yield nth_pentagonal(0)
	for i in range(1,n):
		p =  nth_pentagonal(i)
		if p >= n:
			return
		yield p
		p = nth_pentagonal(-i)
		if p > n:
			return
		yield p


def p(k):
	return p_helper(k+1)

@lru_cache(maxsize=None)
def p_helper(k):
	if k<0:
		return 0
	if k==1:
		return 1
	rval = 0
	signs = [1, 1, -1, -1 ]
	sign_idx = 0
	for pent in gen_gen_pentagonal(k+1):
		rval += signs[sign_idx]*p_helper(k-pent)
		sign_idx = (sign_idx+1)%4
	return rval

for n in range(1,10**6):
	pp = p(n)
	print([n, pp])
	if pp%1000000==0:
		exit()