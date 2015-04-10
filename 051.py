#!python
"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from functools import lru_cache
from math import floor, sqrt

@lru_cache(maxsize=None)
def is_prime(n):
	if n < 2:
		return False
	for i in range(2,floor(sqrt(n))+1):
		if n%i==0:
			return False
	return True

def expand_starred_number(n):
	for i in range(10):
		if n[0]=='*' and i==0:
			continue
		yield int(n.replace('*',str(i)))

def star_string(s):
	if len(s)==1:
		yield '*'
		return
	for i in range(len(s)):
		c = s[i]
		ss = s[:i]+s[i+1:] #strip out each character one at a time
		for j in star_string(ss):
			yield j[:i]+ c +j[i:]
			yield j[:i]+'*'+j[i:]

def prime_sieve(n):
	s=[True for i in range(n)]
	s[0]=False
	for i in range(2,n):
		if s[i-1]:
			for j in range(2*i,n,i):
				s[j-1]=False
			yield i

def enum_with_addl_char(s,c):
	for i in range(len(s)):
		if s[i]!=c:
			yield s[:i]+c+s[i:]
	yield s+c

def enum_with_addl_digit(s):
	for d in range(10):
		for i in enum_with_addl_char(s,str(d)):
			yield i

def is_all_stars(s):
	ss = set(s)
	return len(ss)==1 and '*' in ss

def has_leading_zero(s):
	return s[0]=='0'

def is_yieldable(s):
	return not(has_leading_zero(s))

def enumerate_n_digit_starred_numbers(n):
	if n < 2:
		yield '*'
		return
	for i in enumerate_n_digit_starred_numbers(n-1):
		for j in enum_with_addl_char(i,'*'):
			if is_yieldable(j):
				yield j
		if is_all_stars(i):
			for j in enum_with_addl_digit(i):
				if is_yieldable(j):
					yield j

def endsn(n):
	if n < 2:
		yield '*'
		return
	for i in endsn(n-1):
		for j in range(len(i)):
			for c in list("*0123456789"):
				if i[j]!=c:
					if is_yieldable(i[:j]+c+i[j:]):
						yield i[:j]+c+i[j:]
				if is_yieldable(i+c):
					yield i+c


if __name__=="__main__":
	ps = list(prime_sieve(10000000))
	sp = set(ps)
	target = 8
	for i in range(1,len(str(max(sp)))+1):
		print(i)
		for sn in sorted(list(set(endsn(i)))):
			ll = list(filter(lambda x: (x in sp), expand_starred_number(sn)))
			if len(ll) >= target:
				print(ll)
				exit()