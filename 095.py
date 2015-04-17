#!python
"""
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

from functools import lru_cache

def gen_proper_divisors(x):
	for i in range(1,x):
		if x%i==0:
			yield i

@lru_cache(maxsize=None)
def next_in_chain(x):
	if x==1:
		return 1
	return sum(gen_proper_divisors(x))

def gen_chain(x, max):
	y = next_in_chain(x)
	r = [x]
	while y not in r and y < max:
		r.append(y)
		y = next_in_chain(y)
	if y==x:
		return r
	return []

limit = 1000000

cl = 0
ch = []

for i in range(2, limit):
	c = list(gen_chain(i, limit))
	#print([i,c])
	if len(c) > cl:
		cl = len(c)
		ch = c
		print([i, cl, min(ch)])

print(min(ch))
