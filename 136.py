#!python
"""
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""
from operator import __eq__
from functools import partial

limit = 10**6*50

print('producing array')

soln_count = [0 for i in range(limit+1)]

print('producing values')

for u in range(1,limit+1):
	v=1
	while (u*v)<=limit:
		if (u+v)%4==0 and (3*v)>u and (3*v-u)%4==0:
			soln_count[u*v]+=1
		v+=1

print('filtering list')

print(len(list(filter(partial(__eq__,1), soln_count))))
