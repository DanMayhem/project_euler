#!python
"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""

limit = 1000000

def r(k):
	return int('1'*k)

def a(n):
	i=2
	while r(i)%n!=0:
		i+=1
	return i

def new_a(n):
	i = len(str(n))
	rem = r(i)
	while rem != 0:
		while rem < n:
			i+=1
			rem = rem*10+1
			#print("inner: {0}".format([i, rem]))
		rem = rem % n
		#print("outer: {0}".format([rem//n, rem]))

	return i

n = limit+1

aa = new_a(n)
while aa < limit:
	print([n, aa])
	n+=1
	while n%2==0 or n%5==0:
		n+=1
	aa = new_a(n)

print(n)
exit()


aa = a(n)
while aa < limit:
	print([n, aa])
	n+=1
	while n%2==0 or n%5==0:
		n+=1
	aa = a(n)

print(n)