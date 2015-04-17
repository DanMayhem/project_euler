#!python 
"""
Let W(n,k) be the number of ways in which n can be written as the product of k distinct positive integers.

For example, W(144,4) = 7. There are 7 ways in which 144 can be written as a product of 4 distinct positive integers:

144 = 1×2×4×18
144 = 1×2×8×9
144 = 1×2×3×24
144 = 1×2×6×12
144 = 1×3×4×12
144 = 1×3×6×8
144 = 2×3×4×6
Note that permutations of the integers themselves are not considered distinct.

Furthermore, W(100!,10) modulo 1 000 000 007 = 287549200.

Find W(10000!,30) modulo 1 000 000 007.
"""

from functools import lru_cache
from pe import prime_factors, product
from math import factorial


@lru_cache(maxsize=None)
def c_prime_factors(n):
	return prime_factors(n)

@lru_cache(maxsize=None)
def all_multiplicands(n):
	"taken from problem 88"
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

def W(n, k):
	options = all_multiplicands(n)
	count = 0
	for o in options:
		if len(o)==k:
			count+=1
	return count

print(W(factorial(100),10)%1000000007)