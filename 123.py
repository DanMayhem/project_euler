#!python
"""
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 1010.
"""

from functools import lru_cache
from math import sqrt
from pe import prime_sieve

max_n = 1000000
min_n = 7037
target = 10**10

ps = list(prime_sieve(max_n))

def calc_r(n):
	pn = ps[n-1]
	return ((pn-1)**n+(pn+1)**n)%(pn*pn)


for i in range(min_n, max_n):
	r = calc_r(i)
	print([i, r])
	if r > target:
		print(i)
		exit()