#!python
"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).
"""

from pe import is_prime

def a(n):
	i = 1
	rem = 1
	while rem != 0:
		while rem < n:
			i+=1
			rem = rem*10+1
			#print("inner: {0}".format([i, rem]))
		rem = rem % n
		#print("outer: {0}".format([rem//n, rem]))

	return i


limit = 25

n = 90

s = 0
c = 0

while c < limit:
	while n%2==0 or n%5==0 or is_prime(n):
		n+=1
	aa = a(n)
	if (n-1)%aa==0:
		c += 1
		s += n
		print([c, n, aa, s])
	n+=1
