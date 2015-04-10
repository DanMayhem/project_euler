#!python
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def get_digit_str(x):
	return str(sorted(list(str(x))))

def are_n_multiples_permutations(x, n):
	digits = get_digit_str(x)
	for i in range(1,n+1):
		if digits != get_digit_str(i*x):
			return False
	return True

if __name__=="__main__":
	num_multiples = 6
	for x in range(1,1000000):
		if are_n_multiples_permutations(x,num_multiples):
			print([x, x*2, x*3, x*4, x*5, x*6])
			exit()
