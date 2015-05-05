#!python
"""
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
"""

from fractions import gcd
from functools import lru_cache

from pe import rad, prime_sieve, prime_factors, product

limit = 120000

def is_hit(a, b, c):
	if a >= b:
		return False
	if (a+b)!=c:
		return False
	if gcd(a,b)!=1:
		return False
	if gcd(a,c)!=1:
		return False
	if gcd(b,c)!=1:
		return False
	if rad(a*b*c) < c:
		return True

@lru_cache(maxsize=None)
def prime_factors_c(x):
	return prime_factors(x)

r = 0

pfs = [set() for i in range(limit)]

def make_pfs(n):
	if n < 2:
		return
	for i in range(2,n):
		if len(pfs[i-1])==0:
			for j in range(i,n,i):
				pfs[j-1].add(i)

make_pfs(limit)

@lru_cache(maxsize=None)
def rads(n):
	return product(pfs[n-1])

for c in range(3, limit):
	cf = pfs[c-1]
	for a in range(1,c//2):
		af = pfs[a-1]
		if len(cf&af)==0:
			b = c-a
			bf = pfs[b-1]
			if len(cf&bf)==0 and len(af&bf)==0:
				rad_c = rads(a)*rads(b)*rads(c)
				if rad_c < c:
					r+=c
					print([a,b,c,r])
#101, 727, 828
exit()
#old
for c in range(3,limit):
	cf = set(prime_factors_c(c))
	for a in range(1,c//2):
		af = set(prime_factors_c(a))
		if len(cf&af) == 0:
			b = c-a
			if a < b:
				bf = set(prime_factors_c(b))
				if len(cf&bf)==0 and len(af&bf)==0:
					rad_c = product(af)*product(bf)*product(cf)
					if rad_c < c:
						r+=c
						print([a,b,c,r])


exit()
#old
for a in range(1,limit//2):
	for b in range(a+1,limit-a):
		if is_hit(a,b,a+b):
			r+=a+b
			print([a,b,a+b,r])



