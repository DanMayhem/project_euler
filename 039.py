#!python
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
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

if __name__=="__main__":
	l = 0
	for p in range(1,1000):
		t = list(generate_triples(p))
		if len(t) > l:
			l = len(t)
			print(p)
