#!python
"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

"""

"""
We will have an alternative internal representation of an n-gon
it's a list (l) of 2n elements l[:n] are the outer ring, clockwise,
with l[i] connected to l[i+n]. 
"""

def _find_k(a):
	k=-1
	for i in range(len(a)-1):
		if a[i] < a[i+1]:
			k = i
	return k

def _find_l(a, k):
	l = -1
	for i in range(k+1,len(a)):
		if a[k] < a[i]:
			l=i
	return l

def permutations(l):
	a = l[:]
	a.sort()
	yield a
	k=0
	while k>-1:
		k = _find_k(a)
		if k==-1:
			return
		l = _find_l(a, k)
		x = a[k]
		a[k] = a[l]
		a[l] = x
		a[k+1:] = reversed(a[k+1:])
		yield a


def is_magic_ngon(l):
	n = int(len(l)/2)
	outer = l[:n]
	inner = l[n:]
	target = outer[0]+inner[0]+inner[1]
	for i in range(1,len(outer)):
		if target != outer[i]+inner[i]+inner[(i+1)%n]:
			return False
	return True

def canonical_ngon_representation(l):
	n = int(len(l)/2)
	outer = l[:n]
	inner = l[n:]
	mo = min(outer)
	while mo != outer[0]:
		outer = outer[1:]+[outer[0]]
		inner = inner[1:]+[inner[0]]

	s=""

	for i in range(n):
		s += str(outer[i])+str(inner[i])+str(inner[(i+1)%n])

	return s


if __name__=="__main__":
	#we know 10 must be in the outer ring, let's just put it first in
	#all the permutations, and see what falls out
	l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	ll = []
	for p in permutations(l):
		if is_magic_ngon([10]+p):
			print([p, canonical_ngon_representation([10]+p)])
			ll.append(canonical_ngon_representation([10]+p))

	print(max(ll))



