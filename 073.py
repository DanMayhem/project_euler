#!python
"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

from fractions import Fraction, gcd
from math import floor, ceil
from functools import lru_cache, reduce, partial

def prime_factors(n):
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				yield i
				n = int(n/i)
				break
			i += 1

@lru_cache(maxsize=1024)
def distinct_prime_factors(n):
	return set(prime_factors(n))

@lru_cache(maxsize=1024)
def is_rel_prime(a, b):
	return len(distinct_prime_factors(a) & distinct_prime_factors(b))==0

def gen_farey(n, a=0, b=1, c=1, d=None):
	if d is None:
		d=n
	yield a/b#Fraction(a, b)
	while c <= n:
		k = int((n+b)/d)
		a, b, c, d = c, d, k*c-a, k*d-b
		yield a/b#Fraction(a,b)

def count_fractions(n, x, y, a=0, b=1, c=1, d=None):
	if d is None:
		d=n
	count = 0
	while (not (c==1 and d==2)):
		k = int((n+b)/d)
		a, b, c, d = c, d, k*c-a, k*d-b
		count += 1
	return count

print(count_fractions(12000, 1, 2, 1, 3, 4000, 11999))
exit()

if __name__=="__main__":
	lower = 1/3#Fraction(1,3)
	upper = 1/2#Fraction(1,2)
	max_d = 12000

	count = 0

    
	#used 071 to find a and b
	for f in gen_farey(max_d, 4000, 11999, 1, 3):
		#print(f)
		if f > lower:
			count+=1
		if f >= upper:
			print(count)
			exit()

	exit()
	fs = set([])

	for d in range(1,max_d+1):
		ln = floor(lower*d)
		if Fraction(ln,d)<=lower:
			ln+=1
		un = ceil(upper*d)-1
		if Fraction(un,d)>=upper:
			un-=1
		#print([d, ln, un])
		for n in range(ln, un):
			if gcd(n, d)==1:
				count+=1
			#fs.add(Fraction(n, d))

	print(count)
