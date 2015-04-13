#!python 
"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def num_digits(x):
	return len(str(x))

if __name__=="__main__":
	m = 100
	s = 0
	for i in range(1,m+1):
		j=1
		while num_digits(j**i) <= i:
			if num_digits(j**i) == i:
				s += 1
			j+=1
		print([i, s])
