#!python
"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import Decimal, getcontext
from math import sqrt

getcontext().prec = 200 #give us plenty of precision

def sum_of_first_100_digits(d):
	i = int(d*Decimal(10**100))#ensure we have at least 100 digits
	return sum(map(int, list(str(i)[:100])))

s = 0
for i in range(101):
	if sqrt(i)!=int(sqrt(i)):
		s+= sum_of_first_100_digits(Decimal(i).sqrt())
		print([i, s])