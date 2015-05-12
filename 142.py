#!python
"""
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
"""

from math import sqrt
from functools import lru_cache

"""
a = x+y
b = x-y
c = x+z
d = x-z
e = y+z
f = y-z
ergo 
a,c,d are squares
and
a > d > c
"""

@lru_cache(maxsize=None)
def is_sq(n):
	return n>0 and int(sqrt(n))**2==n


limit = 10**6

for i in range(4,limit):
	a= i*i
	for j in range(2,i):
		c = j*j
		f = a-c
		if not is_sq(f):
			continue
		for k in range(1,j):
			d = k*k
			e = a-d
			b = c-e
			if not is_sq(e):
				continue
			if not is_sq(b):
				continue
			x = (d+c)/2
			if x!=int(x):
				continue
			x = int(x)
			y = (e+f)/2
			if y!=int(y):
				continue
			y = int(y)
			z = (c-d)/2
			if z!=int(z):
				continue
			z = int(z)
			print([x,y,z,x+y+z])
			exit()


for x in range(3,limit):
	for y in range(2,x):
		for z in range(1,y):
			if is_sq(x+y) and is_sq(x-y) and is_sq(x+z) and is_sq(x-z) and is_sq(y+z) and is_sq(y-z):
				print([x,y,z,x+y+z])
				exit()
