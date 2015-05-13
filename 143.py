#!python
"""
Let ABC be a triangle with all interior angles being less than 120 degrees. Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC, the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r. Even more remarkable, it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle. For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli triangles.
"""

from math import sqrt
from functools import lru_cache

#@lru_cache(maxsize=None)
def get_len(a, b):
	return sqrt(a*a+b*b+a*b)

limit = 120000

s = 0
c = 0

sums = set()

for p in range(1,limit):
	for q in range(p,limit-p+1):
		lb = get_len(p,q)
		#print([p,q,lb])
		if lb <=0 or int(lb)!=lb:
			continue
		for r in range(q,limit-p-q+1):
			la = get_len(q, r)
			if la <=0 or int(la)!=la:
				continue
			lc = get_len(p,r)
			if lc <=0 or int(lc)!=lc:
				continue
			c+=1
			s+=(p+q+r)
			sums.ad(p+q+r)
			print([c, la, lb, lc, p, q, r, s])

print(sum(sums))