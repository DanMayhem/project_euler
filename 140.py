#!python
"""
Consider the infinite polynomial series AG(x) = xG1 + x2G2 + x3G3 + ..., where Gk is the kth term of the second order recurrence relation Gk = Gk−1 + Gk−2, G1 = 1 and G2 = 4; that is, 1, 4, 5, 9, 14, 23, ... .

For this problem we shall be concerned with values of x for which AG(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.

x	AG(x)
(√5−1)/4	1
2/5	2
(√22−2)/6	3
(√137−5)/14	4
1/2	5
We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
"""


nuggets = set([2])

starts = [ (0,-1), (0,1), (-3,-2), (-3,2), (-4,-5), (2,-7), (2,7)]

for k, b in starts:
	for i in range(30):
		k, b = -9*k+(-4*b)-14, -20*k-9*b-28
		if k>0:
			nuggets.add(k)

n = sorted(nuggets)[:31]

s = 0

for i in range(len(n)):
	s+=n[i]
	print([i+1,n[i],s])
