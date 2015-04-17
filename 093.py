#!python
"""
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""

from itertools import combinations, permutations, combinations_with_replacement
from operator import add, sub, mul, truediv

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ops  = [add, add, add, sub, sub, sub, mul, mul, mul, truediv, truediv, truediv]
opsx = "+ + + - - - x x / / /".split()
od = {add:'+', sub:'-', mul:'x', truediv:'/'}
eval_order = [0, 1, 2]

def print_expression(d, o):
	print("{0}{1}{2}{3}{4}{5}{6}".format(d[0],od[o[0]],d[1],od[o[1]],d[2],od[o[2]],d[3]))

def eval_expression(d, o):
		return o[2](o[1](o[0](d[0],d[1]), d[2]), d[3])

def eval_all_expressions(d, o):
	a, b, c, d = d
	i, j, k = o

	try:
		yield k(j(i(a,b),c),d)
	except ZeroDivisionError:
		pass
	try:
		yield k(i(a,j(b,c)),d)
	except ZeroDivisionError:
		pass
	try:
		yield i(a,j(b,k(c,d)))
	except ZeroDivisionError:
		pass
	try:
		yield i(a,k(j(b,c),d))
	except ZeroDivisionError:
		pass
	try:
		yield j(i(a,b),k(c,d))
	except ZeroDivisionError:
		pass
	try:
		yield k(i(a,j(b,c)),d)
	except ZeroDivisionError:
		pass



def min_non_expressible(d):
	results = set([])
	for o in permutations(ops, 3):
		for p in permutations(d):
			try:
				for x in eval_all_expressions(p, o):
					if (int(x)==x) and (x > 0) and (x not in results):
						results.add(int(x))
			except ZeroDivisionError:
				pass
	i=1
	#print(results)
	while i in results:
		i+=1
	return i

#print(min_non_expressible((1,2,5,8)))
#exit()

mne=0
for c in combinations(digits,4):
	x = min_non_expressible(c)
	if x > mne:
		mne = x
		print([x, c])





