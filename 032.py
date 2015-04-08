#!python
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from math import ceil, sqrt

def is_pandigital_9(x):
	s=str(x)
	if len(s)!=9:
		return False
	for i in range(1,10):
		if str(i) not in s:
			return False
	return True

def is_pandigital_product(m,n,p):
	return is_pandigital_9(str(m)+str(n)+str(p))

def divisors(x):
	f = []
	if x==2:
		f=[2,1]
	elif x==3:
		f=[3,2,1]
	else:
		for i in range(1,ceil(sqrt(x))):
			if x%i==0:
				f.append(int(x/i))
				yield i
		if sqrt(x) == ceil(sqrt(x)):
			yield(int(sqrt(x)))
	f.reverse()
	for j in f:
		yield int(j)

def pandigital_product_generator():
	for i in range(2,10000):
		for p in divisors(i):
			if is_pandigital_product(p, int(i/p), i):
				yield i
				break

if __name__=="__main__":
	print(sum(pandigital_product_generator()))