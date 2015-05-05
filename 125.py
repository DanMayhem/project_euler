#!python
"""
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.
"""

from math import sqrt, ceil
from itertools import product
from functools import lru_cache

from pe import is_palindrome

limit = 10**8

squares = [i*i for i in range(int(sqrt(limit)))]

def gen_palindromes(max_len):
	if max_len == 1:
		for i in range(1,10):
			yield i
		return
	for i in gen_palindromes(max_len-1):
		yield i
	is_odd = max_len%2==1
	for p in product("0123456789",repeat=ceil(max_len/2)):
		if p[0]!='0':
			if is_odd:
				yield int(''.join(list(p)+list(reversed(p))[1:]))
			else:
				yield int(''.join(list(p)+list(reversed(p))))

@lru_cache(maxsize=None)
def square_sum(i,j):
	return sum(squares[i:j])

def is_cons_sq_sum(n):
	for i in range(1,len(squares)):
		if (i//2)>n:
			return False
		for j in range(i+2,len(squares)):
			ss = square_sum(i,j)
			if ss==n:
				return True
			if ss > n:
				break
	return False

@lru_cache(maxsize=None)
def p(n):
	return int((2*n*n*n+3*n*n+n)/6)

def icss(n):
	for i in range(1,n):
		if p(i)>n:
			return False
		for j in range(i):
			if p(i)-p(j)==n:
				return True
	return False

r = 0

for p in gen_palindromes(len(str(limit))):
	if is_cons_sq_sum(p):
		r+=p
		print([p,r])

i=2

pi=p(i)

sums = set()

while pi <= limit:
	for j in range(i-1):
		pp = pi-p(j)
		if pp not in sums and is_palindrome(pp):
			r+=pp
			sums.add(pp)
			print([pp, r])
	i+=1
	pi =p(i)

