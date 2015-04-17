#!python
"""
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""

from itertools import product

def get_legs_squared(p, q):
	a = p[0]**2+p[1]**2
	b = q[0]**2+q[1]**2
	c = (p[0]-q[0])**2 + (p[1]-q[1])**2
	return (a, b, c)

def is_right(t):
	tt = sorted(t)
	return (tt[0]+tt[1])==tt[2] and 0 not in tt

limit = 50
results = []
for p, q in product(product(range(limit+1), range(limit+1)),product(range(limit+1), range(limit+1))):
	if is_right(get_legs_squared(p, q)):
		if [p,q] not in results and [q,p] not in results:
			results.append([p,q])
			print([p, q])
print(len(results))
