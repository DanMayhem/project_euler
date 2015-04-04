#!python
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(i):
	return i == int(str(i)[::-1])

p = 1

for i in range(100,1000):
	for j in range(100,1000):
		if is_palindrome(i*j) and (i*j) > p:
			p = i*j

print(p)