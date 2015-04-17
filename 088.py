#!python
"""
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""
#the smallest possible k, is 1+1+...+1, i.e. k, however this will not be a product sum for k>1
#also notice that 2xkx1x1x1x...x1 (k-2 ones) == 2k = 2 + k + 1+...+1 (k-2 ones)
#so out minimal product sum is k<=mps<=2k so we just need to look for product sums in this range

from functools import reduce, lru_cache
from operator import mul
from pe import prime_factors

def product(l):
	return reduce(mul, l)

def is_ps(l):
	return sum(l) == product(l)

@lru_cache(maxsize=None)
def c_prime_factors(n):
	return prime_factors(n)

@lru_cache(maxsize=None)
def c_all_multiplicands(n):
	return list(all_multiplicands(n))

@lru_cache(maxsize=None)
def all_multiplicands(n):
	factors = c_prime_factors(n)
	res = []
	if len(factors)==1:
		return [[n]]
	ms = []
	for i in range(len(factors)):
		f = factors[i]
		r = sorted(all_multiplicands(product(factors[:i]+factors[i+1:])))
		if r not in res:
			res.append(r)
			for arr in r:
				farr = sorted([f]+arr)
				if farr not in ms:
					ms.append(farr)
				for j in range(len(arr)):
					farr = sorted(arr[:j]+[f*arr[j]]+arr[j+1:])
					if farr not in ms:
						ms.append(farr)
	return ms

def is_n_ps_for_k(n, k):
	for candidate in all_multiplicands(n):
		if len(candidate) > k:
			continue #this shouldn't really happen
		if(sum(candidate)+k-len(candidate))==n:
			return True
	return False


limit = 12000

s = set([])

for i in range(2,limit+1):
	for j in range(i, 2*i+1):
		if is_n_ps_for_k(j, i):
			print([i, j])
			s.add(j)
			break
print(sum(s))


