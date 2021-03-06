#!python
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

def is_curious(n):
	return (n>2) and (n==sum(map(factorial,map(int,str(n)))))

if __name__=="__main__":
	s=0
	for i in range(1000000):
		if is_curious(i):
			s+=i
	print(s)