#!python
"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.
"""

from math import sqrt, floor
from functools import lru_cache
from fractions import gcd
from pe import generate_primitive_triples

def gen_cuboids(m):
	for i in range(1, m+1):
		for j in range(1, i+1):
			for k in range(1, j+1):
				yield (i, j, k)

@lru_cache(maxsize=None)
def route_len(a, b):
	return sqrt(a*a+b*b)

@lru_cache(maxsize=None)
def shortest_route(i, j, k):
	return min([route_len(i+j, k), route_len(i, j+k), route_len(i+k, j)])

def is_int(i):
	return int(i)==i

def squared_route_len(a, b):
	return a*a+b*b

@lru_cache(maxsize=None)
def shortest_route_is_int(i, j, k):
	return is_int(sqrt(min([squared_route_len(i+j, k), squared_route_len(i+k, j), squared_route_len(j+k, i)])))

@lru_cache(maxsize=None)
def is_ptriple(c, a, b):
	return c*c==a*a+b*b

def is_int_short_route(i, j, k):
	d = gcd(i, gcd(j, k))
	return is_ptriple(int(i/d), int(j/d), int(k/d))



def xcount_of_integer_routes_for_m(m):
	count = 0
	for i, j, k in gen_cuboids(m):
		if is_int_short_route(i, j, k):
			count+=1
	return count

def cuboids_generating_triple(t, m):
	if (t[0]<=m) and (t[1]<=2*m):
		return floor(t[1]/2)
	return 0
	count=0
	a, b = t[0], t[1]
	for i in range(1, m+1):
		for j in range(1, i+1):
			for k in range(1, j+1):
				if ((i+j)==a and k==b) or ((i+j)==b and k==a):
					count+=1
				if ((i+k)==a and j==b) or ((i+k)==b and j==a):
					count+=1
				if ((k+j)==a and i==b) or ((k+j)==b and i==a):
					count+=1
	return count


@lru_cache(maxsize=None)
def count_of_integer_routes_for_m(m):
	if m==0:
		return 0
	count = 0
	l = []
	for t in generate_primitive_triples(int(sqrt(2*m*m))+1):
		i=1
		while (t[0]<=(m/i)) and (t[1]<=(2*m/i)) and (t[2]<=(sqrt(2*m*m)/i)):
			if t not in l:
				l.append(t)
				count+=cuboids_generating_triple(t, m)
			i+=1

	return count + count_of_integer_routes_for_m(m-1)


lower = 439   #estimate
upper = 500  #estimate
target = 1000000


count = 0
l=2
while count < target:
	l+=1
	for wh in range(3,2*l+1):
		path = sqrt(wh*wh+l*l)
		if path==int(path):
			if wh <= l:
				count += floor(wh/2)
			else:
				count += 1 + (l - floor((wh+1)/2))
	print([l, count])
exit()


print(count_of_integer_routes_for_m(100))
#print(sorted(list(generate_primitive_triples(1000))))
exit()
	
while count_of_integer_routes_for_m(upper) < target:
	print(upper)
	lower=upper
	upper*=2
	#exponential count up to find a soln bigger than the target

while lower < upper:
	b = int((upper+lower)/2)
	count = count_of_integer_routes_for_m(b)
	if count > target:
		upper = b
	else:
		lower = b
	print([lower, upper, b, count])