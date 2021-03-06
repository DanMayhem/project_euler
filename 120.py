#!python
"""
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
"""

def r(a,n):
	return ((a-1)**n+(a+1)**n)%(a*a)

def rmax(a):
	return 2*a*((a-1)//2)

print(sum(map(rmax, range(3,1001))))

exit()

ss = 0
for a in range(3,1001):
	rmax = 0
	for n in range(1,1000):
		rr = r(a,n)
		if rr > rmax:
			rmax = rr
	print([a,rmax])
	ss+=rmax
print(ss)