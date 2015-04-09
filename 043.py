#!python
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

def _find_k(a):
	k=-1
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			k = i
	return k

def _find_l(a, k):
	l = -1
	for i in range(k+1,len(a)):
		if a[k] > a[i]:
			l=i
	return l

def gen_pandigital_n0_desc(n):
	a = list(reversed([i for i in range(n+1)]))
	yield int(''.join(map(str,a)))
	k=0
	while k>-1:
		k = _find_k(a)
		l = _find_l(a, k)
		x = a[k]
		a[k] = a[l]
		a[l] = x
		a[k+1:] = reversed(a[k+1:])
		if a[0]==0:
			return
		yield int(''.join(map(str,a)))

def is_interesting(n):
	a = str(n)
	if len(a) != 10:
		return False
	if int(a[1:4])%2 != 0:
		return False
	if int(a[2:5])%3 != 0:
		return False
	if int(a[3:6])%5 != 0:
		return False
	if int(a[4:7])%7 != 0:
		return False
	if int(a[5:8])%11 != 0:
		return False
	if int(a[6:9])%13 != 0:
		return False
	if int(a[7:10])%17 != 0:
		return False
	return True

if __name__=="__main__":
	print(sum(filter(is_interesting,gen_pandigital_n0_desc(9))))
