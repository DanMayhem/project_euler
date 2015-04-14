#!python
"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

from math import sqrt
from functools import lru_cache, partial

@lru_cache(maxsize=None)
def is_octagonal(n):
	x = (2+sqrt(4+12*n))/6
	y = (2-sqrt(4+12*n))/6
	return (x>0) and (x==int(x)) or (y>0)and(y==int(y))

@lru_cache(maxsize=None)
def is_heptagonal(n):
	x = (3+sqrt(9+40*n))/10
	y = (3-sqrt(9+40*n))/10
	return (x>0) and (x==int(x)) or (y>0)and(y==int(y))

@lru_cache(maxsize=None)
def is_hexagonal(n):
	x = (1+sqrt(1+8*n))/4
	y = (1-sqrt(1+8*n))/4
	return (x>0) and (x==int(x)) or (y>0)and(y==int(y))

@lru_cache(maxsize=None)
def is_pentagonal(n):
	x = (1+sqrt(1+24*n))/6
	y = (1-sqrt(1+24*n))/6
	return (x>0) and (x==int(x)) or (y>0)and(y==int(y))

@lru_cache(maxsize=None)
def is_square(n):
	return int(sqrt(n))==sqrt(n)

@lru_cache(maxsize=None)
def is_triangular(n):
	x = (-1+sqrt(1+8*n))/2
	y = (-1-sqrt(1+8*n))/2
	return (x==int(x)) or (y==int(y))

def get_cycle_candidates(n, l):
	def _is_cycle_candidate(x):
		return str(n)[-2:]==str(x)[:2]
	ll= list(filter(_is_cycle_candidate, l))
	#print([n, l, ll])
	return ll

def can_chain_from(n, l):
	return str(n)[-2:]==str(l[0])[:2]


def fis(ss):
	if len(ss)==1:
		for s in ss[0]:
			yield [s]
		return
	for i in range(len(ss)):
		#filter the remaing sets to find cyclical candidates
		for j in range(len(ss[i])):
			#try to find a cyclical set for each number in ss[i], ie ss[i][j]
			ns = []
			for k in range(len(ss)):
				if i!=k:
					ns.append(ss[k])
			#now we have filtered sets for our subsets
			#recurse
			for l in fis(ns):
				#determin if this sub chain can chain off ss[i][j]
				if can_chain_from(ss[i][j], l):
					yield [ss[i][j]]+l

def can_chain_numbers(a, b):
	return str(a)[-2:]==str(b)[:2]

def fisc(c, ss):
	if len(ss)==1:
		for s in ss[0]:
			if can_chain_numbers(c, s):
				yield [s]
		return
	for i in range(len(ss)):
		#filter the remaing sets to find cyclical candidates
		for j in range(len(ss[i])):
			if can_chain_numbers(c, ss[i][j]):
			#try to find a cyclical set for each number in ss[i], ie ss[i][j]
				ns = []
				for k in range(len(ss)):
					if i!=k:
						ns.append(ss[k])
				#now we have filtered sets for our subsets
				#recurse
				for l in fisc(ss[i][j],ns):
					yield [ss[i][j]]+l

def fiscc(ss):
	nss = ss[1:]
	for c in ss[0]:
		for l in fisc(c, nss):
			yield [c]+l

if __name__=="__main__":
	n3 = list(filter(is_triangular, range(1000,10000)))
	n4 = list(filter(is_square, range(1000,10000)))
	n5 = list(filter(is_pentagonal, range(1000,10000)))
	n6 = list(filter(is_hexagonal, range(1000,10000)))
	n7 = list(filter(is_heptagonal, range(1000,10000)))
	n8 = list(filter(is_octagonal, range(1000,10000)))

	for l in fiscc([n3, n4, n5, n6, n7, n8]):
		#check to see if it's a cycle or just a chain
		if can_chain_from(l[-1], l):
			print([sum(l), l])
