#!python
"""
In the following equation x, y, and n are positive integers.

1
x
+	
1
y
=	
1
n
It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
"""

from pe import prime_sieve, product

primes = list(prime_sieve(45))
exponents = [0 for i in primes]

upper = product(primes)

limit = 4000000
xlimit = 2*limit-1

def find_exp_for_2():
	divisors = 1
	for e in exponents[1:]:
		divisors *= 2*e+1
	exponents[0] = (xlimit//divisors - 1) // 2
	while divisors*(2*exponents[0]+1) < xlimit:
		exponents[0]+=1

def calculate_number():
	r = 1
	for i in range(len(primes)):
		r*= primes[i]**exponents[i]
	return r

def reset_exp(i):
	for j in range(i):
		exponents[j]=exponents[i]

i = 1

while i<len(primes):
	find_exp_for_2()
	if exponents[0]<exponents[1]:
		i+=1
	else:
		n = calculate_number()
		if n < upper:
			upper = n
		i=1
	if i < len(exponents):
		exponents[i]+=1
		reset_exp(i)

print(upper)