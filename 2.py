from functools import reduce

class Fib():
	def __init__(self, max):
		self.a = None
		self.b = 1
		self.max = max

	def __iter__(self):
		return self

	def __next__(self):
		if self.a is None:
			self.a = self.b
			self.b = 1
			return 1
		r = self.a + self.b
		if r > self.max:
			raise StopIteration
		self.a = self.b
		self.b = r
		return r


print(reduce(lambda x, y: x+y, filter(lambda i: i%2==0,Fib(4000000))))