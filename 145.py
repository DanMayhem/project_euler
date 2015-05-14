#!python
"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
"""

from itertools import product

rd = [
	[1,3,5,7,9],
	[0,2,4,6,8],
	[1,3,5,7],
	[0,2,4,6],
	[1,3,5],
	[0,2,4],
	[1,3],
	[0,2],
	[1],
	[0]
	]

digits = [0,1,2,3,4,5,6,7,8,9]

def reverse(x):
	return int(str(x)[::-1])

_odd_digits = {1,3,5,7,9}
_even_digits = {0,2,4,6,8}
def is_all_odd(x):

	digs = set(map(int, list(str(x))))
	return len(digs-_odd_digits)==0

def gen_reversible_list(l):
	if len(l)==1:
		for d in rd[l[0]]:
			yield [l[0],d]
	x = l[0]
	l = l[1:]
	for d in rd[x]:
		for ll in gen_reversible_list(l):
			yield [x]+ll+[d]

def gen_reversible(e):
	if e<=1:
		return
	for r in gen_reversible(e-1):
		yield r
	if e%2==1:
		return
	for i in map(list, product(digits,repeat=e//2)):
		for r in gen_reversible_list(i):
			if r[0]!=0 and r[-1]!=0:
				yield int(''.join(map(str, r)))


# limit=3
# c=0
# for r in gen_reversible(limit):
# 	c+=1
# 	print([c,r])

# exit()


limit = 10**9

c = 0

for i in range(limit):
	if i%10!=0:
		if is_all_odd(i+reverse(i)):
			c+=1
			print([c,i])

