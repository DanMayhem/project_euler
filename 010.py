#!python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from functools import partial, reduce
from operator import add, mod
from math import sqrt

class PrimesLtN:
	def __init__(self, n):
		self.n = n
		self.p=[]
		self.i = 2

	def _has_factor(self, x):
		for i in self.p:
			if x%i==0:
				return True
		return False

	def __iter__(self):
		return self

	def __next__(self):
		while(self._has_factor(self.i)):
			self.i = self.i+1
		if self.i > self.n:
			raise StopIteration()
		self.p.append(self.i)
		return self.i

if __name__=="__main__":
	print(reduce(add, PrimesLtN(2000000)))