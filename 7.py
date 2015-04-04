#!python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from functools import partial
from operator import add, mod

class NthPrime:
	def __init__(self, n):
		self.n = n
		self.p=[]
		self.i = 2

	def _has_factor(self, x):
		x_mod = partial(mod, x)
		return 0 in map(x_mod,self.p)

	def __iter__(self):
		return self

	def __next__(self):
		if len(self.p) >= self.n:
			raise StopIteration()
		while(self._has_factor(self.i)):
			self.i = self.i+1
		self.p.append(self.i)
		return self.i


print(list(NthPrime(10001))[-1])

