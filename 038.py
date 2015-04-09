#!python
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def is_pandigital(x):
	s = list(str(x))
	s.sort()
	for i in range(len(s)):
		if str(i+1) != s[i]:
			return False
	return True

def concatenated_product(x, l):
	cp = ""
	for m in l:
		cp += str(x*m)
	return int(cp)

def is_9_digit(n):
	return (n >= 100000000) and (n <= 999999999)

if __name__=="__main__":
	for i in range(2,10000):
		for j in range(2,100):
			cp = concatenated_product(i,range(1,j+1))
			if is_9_digit(cp) and is_pandigital(cp):
				print(cp)

