#!python
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

from functools import lru_cache
from math import floor, sqrt

def nw_diags(n):
	for i in range(3, n+1, 2):
		yield i*i - 2*i + 2


def sw_diags(n):
	for i in range(3,n+1,2):
		yield i*(i-1)+1


def se_diags(n):
	for i in range(1,n+1,2):
		yield i*i

def ne_diags(n):
	for i in range(3, n+1, 2):
		yield (i-2)**2 + i - 1

@lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

if __name__=="__main__":
	diags = set([1])
	prime_count = 0
	diags_count = 1
	for i in range(3, 100001, 2):
		if is_prime(i*i -2*i +2):
			prime_count += 1
		if is_prime(i*(i-1)+1):
			prime_count += 1
		if is_prime((i-2)**2 + i - 1):
			prime_count += 1
		diags_count += 4
		prime_pcnt = prime_count / diags_count
		print("{0}: {1}".format(i, prime_pcnt))
		if prime_pcnt <= .1:
			exit()

