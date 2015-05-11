#!python
"""
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).
"""

from fractions import gcd
from math import sqrt

def is_square(x):
	return int(sqrt(x))**2==x

limit = 10**12
results = set()

for a in range(2,10000):
	for b in range(1,a):
		if a*a*a*b*b+b*b >= limit:
			break
		if gcd(a,b) != 1:
			continue
		c=1
		n = a*a*a*b*c*c+c*b*b
		while n < limit:
			if is_square(n):
				results.add(n)
			c+=1
			n = a*a*a*b*c*c+c*b*b

print(sum(results))