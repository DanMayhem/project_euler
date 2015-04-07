#!python
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import floor, sqrt, ceil

def divisors(x):
	f = []
	if x==2:
		f=[2,1]
	elif x==3:
		f=[3,2,1]
	else:
		for i in range(1,ceil(sqrt(x))):
			if x%i==0:
				f.append(int(x/i))
				yield i
		if sqrt(x) == ceil(sqrt(x)):
			yield(int(sqrt(x)))
	f.reverse()
	for j in f:
		yield int(j)

def d(n):
	return sum(divisors(n))-n

def is_abundant(n):
	return n < d(n)

if __name__=='__main__':
	#generate list of abundant numbers < n/2.
	#abundants = list(filter(is_abundant, range(28123)))
	abundants = []
	s=0
	for i in range(28123):
		t=i
		half_i = floor(i/2)
		if is_abundant(i):
			abundants.append(i)
		for a in abundants:
			if a>half_i:
				break
			if (i-a) in abundants:
				t=0
				break
		s+=t
	print (s)




