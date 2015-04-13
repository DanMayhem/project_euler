#!python
"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

from math import floor, sqrt
from fractions import Fraction

def get_expansion(s):
	m = 0
	d = 1
	a0 = floor(sqrt(s))
	a = a0
	terms = []
	triples = []
	mp = None
	dp = None
	ap = None
	while (m, d, a) not in triples:
		triples.append((m, d, a))
		mp = m
		dp = d
		ap = a
		m = dp*ap-mp
		d = (s-m*m)/dp
		a = floor((a0+m)/d)
		terms.append(a)
	return [a0] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1] + terms[:-1]

def expand_continued(c):
	f = Fraction(c[0])

	if len(c) == 1:
		return f

	return f + Fraction(1, expand_continued(c[1:]))

def gen_convergents(e):
	for i in range(len(e)):
		yield expand_continued(e[:i+1])

def minimal_soln_in_x(d):
	for c in gen_convergents(get_expansion(d)):
		if is_diophantine_soln(c.numerator, c.denominator, d):
			return c.numerator

def is_diophantine_soln(x, y, d):
	return x*x-d*y*y == 1

def is_not_square(n):
	return sqrt(n)!=int(sqrt(n))

m=1000

d_range = list(filter(is_not_square, range(2,m)))

if __name__=="__main__":
	mi = 0 
	mx = 0
	for i in d_range:
		x = minimal_soln_in_x(i)
		if x > mx:
			mi = i
			mx = x
	print(mi)