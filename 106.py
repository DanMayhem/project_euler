#!python
"""
Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
"""

from itertools import combinations

n=12
a = set([i for i in range(n)])
k=0

def must_check_set(a, b):
	if len(a)!=len(b):
		return True
	a = sorted(a)
	b = sorted(b)
	if a[0] > b[0]:
		a, b = b, a
	if max(a)<min(b):
		return False
	for i in range(len(a)):
		if a[i] > b[i]:
			return True
	return False

for i in range(2,len(a)//2+1):
	for b in combinations(a, i):
		b = set(b)
		x = a-b
		for c in combinations(x, i):
			if must_check_set(b, c):
				k+=1
				print([k/2,b,c])