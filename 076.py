#!python
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from math import floor, ceil
from functools import lru_cache

@lru_cache(maxsize=8196)
def n_terms_sum_to_a(a, n):
	#print([a, n,'.'])
	if n==1:
		return [[a]]
	collection = []
	for i in range(1, a):
		#print([a,n,i])
		for l in n_terms_sum_to_a(a-i, n-1):
			if i >= max(l):
				collection.append([i]+l)
	return collection


@lru_cache(maxsize=4096)
def n_terms_sum_to_a_count(a, n, m):
	#print([a, n, m])
	if n==1:
		if a <= m and a>0:
			return 1
		return 0
	collection = 0
	for i in range(1,min([a, m+1])):
		#print([a,n,i])
		collection+= n_terms_sum_to_a_count(a-i, n-1, min([m, i]))
	return collection

limit = 100
count = 0 

def count_only():
	global count, limit
	for i in range(2,limit+1):
		count += (n_terms_sum_to_a_count(limit, i, limit))
		print(count)

def full_enum():
	global count, limit
	for i in range(2, limit+1):
		l = n_terms_sum_to_a(limit, i)
		count += len(l)
		print(count)

count_only()
#full_enum()