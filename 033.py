#!python
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from math import sqrt, ceil
from operator import mul
from functools import reduce
from fractions import gcd

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

def is_curious(n, d):
	n_d = set(map(int,str(n))) #set of digits in numerator
	d_d = set(map(int,str(d))) #set of digits in denominator
	dig = n_d & d_d #set of common digits
	dig = dig - set([0]) #not interested in trivial examples
	if len(dig)>0:
		for digit in dig:
			n_prime = int(str(n).replace(str(digit),'',1))
			d_prime = int(str(d).replace(str(digit),'',1))
			if (d_prime!=0) and ((n/d)==(n_prime/d_prime)):
				return True
	return False




if __name__=="__main__":
	ns=[]
	ds=[]
	for d in range(11,100):
		for n in range(11,d):
			if is_curious(n,d):
				ns.append(n)
				ds.append(d)
	n = reduce(mul,ns)
	d = reduce(mul,ds)
	x = gcd(n,d)
	if x != 0:
		d /= x
	print(d)