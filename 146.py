#!python
"""
The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
"""

from functools import lru_cache
from pe import is_prime

@lru_cache(maxsize=100)
def is_prime_c(p):
	return is_prime(p)

def _witness(a, n):
	t = 0
	u = n-1
	while u%2==1:
		u = u//2
	xi1 = pow(a,u,n)
	for i in range(t):
		xi2 = xi1*xi1%n
		if (xi2==1) and (xi1!=1) and (xi1!=(n-1)):
			return True
		xi1=xi2
	if xi1!=1:
		return True
	return False

def _isProbablePrime(n, ar):
	for i in ar:
		if _witness(i, n):
			return False
	return True

@lru_cache(maxsize=100)
def isProbablePrime(n):
	if n < 1373653:
		return _isProbablePrime(n, [2,3])
	if n < 9080191:
		return _isProbablePrime(n, [31,73])
	if n < 4759123141:
		return _isProbablePrime(n, [2,7,61])
	if n < 2152302898748:
		return _isProbablePrime(n, [2,3,5,7,11])
	if n < 3474749660383:
		return _isProbablePrime(n, [2,3,5,7,11,13])
	return _isProbablePrime(n, [2,3,5,7,11,13,17])


limit = 10**6*150

s = 0

for i in range(10,limit,10):
	ii = i*i
	if ii%3 != 1:
		continue

	if ii%7 != 2 and ii%7 != 3:
		continue

	if ii%9==0 or ii%13==0 or ii%27 == 0:
		continue

	if isProbablePrime(ii+1) and isProbablePrime(ii+3) and isProbablePrime(ii+7) and isProbablePrime(ii+9) and isProbablePrime(ii+13) and not isProbablePrime(ii+19) and not isProbablePrime(ii+21) and isProbablePrime(ii+27):
		s+=i
		print([i,s])
