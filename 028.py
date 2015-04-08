#!python
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from math import ceil

class NumberSpiral:
	def __init__(self, size):
		self.size = size
		self.spiral = [[None for i in range(size)] for i in range(size)]
		
		n = size*size - 1
		r=0
		c = size-1
		d="left"
		self.spiral[r][c]=size*size
		while n>0:
			if d=="left":
				if (c>0) and (self.spiral[r][c-1] is None):
					c-=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="down"
			elif d=="down":
				if (r<size-1) and (self.spiral[r+1][c] is None):
					r+=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="right"
			elif d=="right":
				if (c<size-1) and (self.spiral[r][c+1] is None):
					c+=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="up"
			elif d=="up":
				if (r>0) and (self.spiral[r-1][c] is None):
					r-=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="left"

	def get(self, r,c):
		return self.spiral[r][c]


if __name__=="__main__":
	size=1001
	s=0
	ns = NumberSpiral(size)
	for i in range(size):
		s += ns.get(i,i)
		s += ns.get(size-i-1,i)
	print(s-1)

