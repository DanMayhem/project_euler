#!python
"""
Consider the isosceles triangle with base length, b = 16, and legs, L = 17.


By using the Pythagorean theorem it can be seen that the height of the triangle, h = √(172 − 82) = 15, which is one less than the base length.

With b = 272 and L = 305, we get h = 273, which is one more than the base length, and this is the second smallest isosceles triangle with the property that h = b ± 1.

Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and b, L are positive integers.
"""

from math import sqrt

def get_l(b, h):
	return sqrt(b/2*b/2+h*h)

def is_int(i):
	return int(i)==i

target = 12

b = 16
s = 0
c = 0


result = 0
x = 0
y = -1

for i in range(12):
	xnew = -9*x+(-4*y)+4
	ynew = -20*x+(-9*y)+8

	x, y = xnew, ynew

	result += abs(y)
	print([i+1,y,result])

exit()

while c<target:
	l = get_l(b,b-1)
	if is_int(l):
		l = int(l)
		c+=1
		s+=l
		print([c, b, l, s])
	l = get_l(b,b+1)
	if is_int(l):
		l = int(l)
		c+=1
		s+=l
		print([c, b, l, s])
	b+=1
