#!python
"""
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime factors is 9414.

Find the sum of the first forty prime factors of R(109).
"""

from pe import prime_sieve

def gen_prime_factors(n):
	factors = []
	while n>1:
		i=2
		while i<=n:
			if n%i==0:
				yield i
				factors.append(i)
				n = int(n/i)
				break
			i += 1
	return

limit = 40

i=0
s = 0
k = 10**9

for p in prime_sieve(200000):
	if pow(10,k,9*p)==1:
		i+=1
		s+=p
		print([i,p,s])

exit()

r = (10**10**9-1)/9

for f in gen_prime_factors(r):
	s += f
	i += 1
	print([i, f, s])

