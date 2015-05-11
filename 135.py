#!python
"""
Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
"""

from operator import __eq__
from functools import partial

limit = 10**6

soln_count = [0 for i in range(limit+1)]

for u in range(1,limit+1):
	v=1
	while (u*v)<=limit:
		if (u+v)%4==0 and (3*v)>u and (3*v-u)%4==0:
			soln_count[u*v]+=1
		v+=1

print(len(list(filter(partial(__eq__,10), soln_count))))
