#!python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

if __name__=="__main__":
	for c in range(3,998):
		for b in range(2,c):
			for a in range(1,b):
				if a+b+c==1000 and a*a+b*b==c*c:
					print("%d,%d,%d:%d"%(a,b,c,a*b*c))