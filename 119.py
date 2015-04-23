#!python
"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""

from math import log

def is_dps(n):
	s = sum(map(int, list(str(n))))
	i=1
	if s == 1:
		return False
	x = log(n,s)
	return x==int(x)

n=1
a=10

dps_numbers = []

def digit_sum(n):
	return sum(map(int, list(str(n))))

for b in range(2,400):
	for e in range(1,50):
		x = b**e
		if x > 10 and digit_sum(x)==b:
			dps_numbers.append(x)

dps_numbers.sort()
print(dps_numbers[29])

exit()

while n<30:
	if is_dps(a):
		print([n, a])
		n+=1
	a+=1

