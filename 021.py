#!python
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt, floor

def divisors(x):
	f = []
	if x==2:
		f=[2,1]
	if x==3:
		f=[3,2,1]
	for i in range(1,floor(sqrt(x))):
		if x%i==0:
			f.append(int(x/i))
			yield i
	if sqrt(x) == floor(sqrt(x)):
		yield(int(sqrt(x)))
	f.reverse()
	for j in f:
		yield int(j)

def d(n):
	return sum(divisors(n))-n

if __name__=="__main__":
	s = 0
	for i in range(10000):
		j = d(i)
		if(j!=i)and(d(j)==i):
			s+=i
	print(s)