#!python
"""
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
"""

from functools import lru_cache
from itertools import combinations, permutations
from pe import prime_sieve, is_prime

digits = set(list("123456789"))

@lru_cache(maxsize=None)
def is_prime_c(n):
	return is_prime(n)

def build_prime_sets(d):
	count = 0
	if len(d)==0:
		return 1
	for i in range(1,len(d)):
		for c in combinations(d,i):
			for p in permutations(c):
				if is_prime_c(int(''.join(p))):
					count += build_prime_sets(set(d)-set(p))
	return count

def gen_prime_sets(d):
	for p in permutations(d):
		if is_prime_c(int(''.join(p))):
			yield {int(''.join(p))}
	for i in range(1,len(d)//2+1):
		for c in combinations(d, i):
			for p in permutations(c):
				if is_prime_c(int(''.join(p))):
					for ps in gen_prime_sets(set(d)-set(p)):
						ps.add(int(''.join(p)))
						yield ps

ss = []
for s in gen_prime_sets(digits):
	if s not in ss:
		ss.append(s)
		print([len(ss), s])