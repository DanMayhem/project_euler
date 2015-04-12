#!python
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

class NumberSpiral:
	def __init__(self, size,):
		self.size = size
		self.spiral = [[None for i in range(size)] for i in range(size)]
		self._fill_sprial()

	def expand(self):
		self.size += 2
		for row in self.sprial:
			row.insert(0,None)
			row.append(None)
		self.sprial.insert(0,[None for i in range(self.size)])
		self.spiral.append([None for i in range(self.size)])
		self._fill_spiral()

		
	def _fill_spiral(self):
		n = self.size*self.size - 1
		r = self.size-1
		c = self.size-1
		d = "left"
		self.spiral[r][c]=self.size*self.size
		while n>0:
			if d=="left":
				if (c>0) and (self.spiral[r][c-1] is None):
					c-=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="up"
			elif d=="down":
				if (r<size-1) and (self.spiral[r+1][c] is None):
					r+=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="left"
			elif d=="right":
				if (c<size-1) and (self.spiral[r][c+1] is None):
					c+=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="down"
			elif d=="up":
				if (r>0) and (self.spiral[r-1][c] is None):
					r-=1
					self.spiral[r][c]=n
					n-=1
				else:
					d="right"

	def get(self, r,c):
		return self.spiral[r][c]
