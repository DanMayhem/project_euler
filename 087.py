#!python
"""
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

from pe import prime_sieve

ps = list(prime_sieve(1000000))

limit = 50000000

s = set([])

for i in range(len(ps)):
	a = ps[i]**2
	if a < limit:
		for j in range(len(ps)):
			b = ps[j]**3
			if (a+b) < limit:
				for k in range(len(ps)):
					x = a + b + ps[k]**4
					if x < limit:
						s.add(x)
					if x > limit:
						break
			else:
				break
	else:
		break

print(len(s))