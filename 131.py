#!python
"""
There are some prime values, p, for which there exists a positive integer, n, such that the expression n3 + n2p is a perfect cube.

For example, when p = 19, 83 + 82×19 = 123.

What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?
"""

from pe import prime_sieve, is_prime

limit = 1000000

primes = set(prime_sieve(limit))
cubes = set([i**3 for i in range(1,limit)])

c = 0


for i in range(1,577):
	if is_prime((i+1)*(i+1)*(i+1)-i*i*i):
		c+=1
		print([c, i])

exit()

for n in range(1,limit*2):
	for p in primes:
		if (n**3+n*n*p) in cubes:
			c+=1
			print([c, p, n])

exit()
for p in primes:
	for n in range(1,2*p):
		if (n**3+n*n*p) in cubes:
			c+=1
		print([c, p, n])
