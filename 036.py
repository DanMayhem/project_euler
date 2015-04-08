#!python
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(i):
	return i == int(str(i)[::-1])

def is_binary_palindrome(i):
	fmt = "{0:b}"
	return fmt.format(i) == fmt.format(i)[::-1]

def dual_palindromes(max):
	for i in range(max):
		if is_palindrome(i) and is_binary_palindrome(i):
			yield i

if __name__=="__main__":
	print(sum(dual_palindromes(1000000)))