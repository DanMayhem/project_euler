#!python
"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
"""

from math import floor

def is_triple(a,b,c):
	return a*a+b*b==c*c

def generate_triples(p):
	for c in range(1,p):
		for a in range(1,c):
			b = p-c-a
			if a>b:
				continue
			if is_triple(a,b,c):
				yield [a,b,c]

def has_one_triple(p):
	count = 0
	for t in generate_triples(p):
		count +=1
		if count > 1:
			return False
	if count==1:
		return True
	return False

def triple_sieve(p):
	s=[True for i in range(p+1)]
	s[0]= False
	for i in range(1,p+1):
		if s[i]:
			if has_one_triple(i):
				print(i)
				for j in range(i+i, p+1, i):
					s[j]=False
			else:
				s[i]==False


from fractions import gcd
from functools import lru_cache
from math import sqrt

def prime_factors(n):
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				yield i
				n = int(n/i)
				break
			i += 1

def distinct_prime_factors(n):
	return set(prime_factors(n))

def lesser_rel_prime_generator(x):
	l = [True for i in range(x)]
	l[0] = False
	for p in distinct_prime_factors(x):
		for i in range(p+p, x, p):
			l[i]=False

	for i in range(x):
		if l[i]:
			yield i


def generate_primative_triples(limit):
	results = [0 for i in range(limit+1)]
	count = 0
	for m in range(2,int(sqrt(limit/2))):
		for n in range(1,m):
			if(m-n)%2==1:
				if gcd(m,n)==1:
					a = m*m-n*n
					b = 2*m*n
					c = m*m+n*n
					p = a+b+c
					while p <= limit:
						results[p] += 1
						if results[p] == 1:
							count += 1
						if results[p] == 2:
							count -= 1
						p += (a+b+c)
	print(count)

generate_primative_triples(1500000)