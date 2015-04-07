#!python
"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
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
		l = _find_l(a, k)
		x = a[k]
		a[k] = a[l]
		a[l] = x
		a[k+1:] = reversed(a[k+1:])
		yield a


if __name__=="__main__":
	l = [0,1,2,3,4,5,6,7,8,9]
	i=1
	for p in permutations(l):
		if i==1000000:
			print("".join(map(str,p)))
			exit()
		i+=1
