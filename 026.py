#!python
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from math import floor

def find_cycle_len(d):
	remainders = {}
	#find initial remainder
	i=1
	while i < d:
		i*=10
	r = i%d
	while r != 0:
		i=r
		while i<d:
			i*=10
		s = i%d
		remainders[r]=s
		r=s
		if s in remainders:
			#we've found a loop
			i=1
			while remainders[s] != r:
				i+=1
				s = remainders[s]
			return i
	return 0

if __name__=="__main__":
	d = 0
	l = 0
	for i in range(2,1000):		
		x  = find_cycle_len(i)
		if x>l:
			l=x
			d=i
	print(d)
	print(find_cycle_len(d))