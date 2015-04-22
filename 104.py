#!python
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
from math import sqrt, floor
from pe import fib, is_pandigital

phi = (1+sqrt(5))/2

def nth_fib(n):
	return int(phi**n/sqrt(5)+(1/2))


fn2 = 1
fn1 = 1
tailcut = 1000000000
n = 2
fn = 0
found = False

i=1
for f in fib(None):
	print(i)
	i+=1
	if i>100 and is_pandigital(str(f)[:9]) and is_pandigital(str(f)[-9:]):
		exit()
