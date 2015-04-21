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
For n = 4 there are exactly three distinct solutions:

1
5
+	
1
20
=	
1
4
1
6
+	
1
12
=	
1
4
1
8
+	
1
8
=	
1
4
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
"""

from pe import prime_sieve, product

primes = list(prime_sieve(45))
exponents = [0 for i in primes]

upper = product(primes)

limit = 1000
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