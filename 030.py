#!python
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def _sum_of_digits_to_nth(b,n):
	def _mypow(x):
		return (int(x))**n
	return sum(map(_mypow, str(b)))

def nth_power_of_digits(n):
	for i in range(2,10**(n+1)): #what is the correct upper bound?
		if _sum_of_digits_to_nth(i,n)==i:
			yield i


if __name__=="__main__":
	print(sum((nth_power_of_digits(5))))