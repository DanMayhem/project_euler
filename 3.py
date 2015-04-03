
class PrimeFactors():
	def __init__(self, x):
		self.x = x
		self.pf = []
		self.pfp = 1

	def __iter__(self):
		return self

	def __next__(self):
		y = self.x / self.pfp

		#find the next factor of y. the least factor of a composite must be prime
		i = 2
		while(i<sqrt(y))