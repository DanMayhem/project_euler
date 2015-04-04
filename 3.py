#!python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

class PrimeFactors():
	def __init__(self, x):
		self.x = x
		self.pfp = 1

	def __iter__(self):
		return self

	def __next__(self):
		y = self.x / self.pfp

		if y == 1:
			raise StopIteration()

		#find the next factor of y. the least factor of a composite must be prime
		i = 2
		while(i<=y):
			if y%i == 0:
				self.pfp = self.pfp * i
				return i
			i = i+1


if __name__=='__main__':
	print(max(PrimeFactors(600851475143)))

