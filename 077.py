#!python
"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
from math import floor, ceil
from functools import lru_cache



def prime_sieve(n):
	if n < 2:
		return
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

primes = list(prime_sieve(10**6))

prime_set = set(primes)

def is_prime(p):
	return p in prime_set

def primes_range(p, q):
	i=0
	while primes[i] < p:
		i+=1
	j=i
	while primes[j] < q:
		j+=1
	return primes[i:j]

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
		if a <= m and a>0 and is_prime(a):
			return 1
		return 0
	collection = 0
	for i in primes_range(1,min([a, m+1])):
		#print([a,n,i])
		collection+= n_terms_sum_to_a_count(a-i, n-1, min([m, i]))
	return collection

limit = 10
count = 0 

def count_only():
	for x in range(10,100000):
		count = 0
		for i in range(2,x+1):
			count += (n_terms_sum_to_a_count(x, i, x))
		print([x, count])
		if count > 5000:
			exit()

def full_enum():
	global count, limit
	for i in range(2, limit+1):
		l = n_terms_sum_to_a(limit, i)
		count += len(l)
		print(count)

count_only()
#full_enum()