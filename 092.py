#!python
"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from functools import lru_cache

def square(n):
	return n*n

def next_in_chain(n):
	return sum(map(square, map(int, list(str(n)))))

@lru_cache(maxsize=None)
def chains_to_89(n):
	if n==1:
		return False
	if n==89:
		return True
	return chains_to_89(next_in_chain(n))

limit = 10000000
count=0

for i in range(1, limit):
	if chains_to_89(i):
		#print(i)
		count+=1

print(count)