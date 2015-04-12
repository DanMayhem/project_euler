#!ptyhon 
"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

from fractions import Fraction

def nth_term_of_sqrt_2(n):
	f = Fraction(1/2)
	two = Fraction(2)
	for i in range(1,n):
		f = Fraction(1, two+f)

	return Fraction(1)+f

def gen_sqrt_2_terms(n):
	f = Fraction(1/2)
	one = Fraction(1)
	two = Fraction(2)
	yield one + f
	for i in range(n):
		f = Fraction(1, two+f)
		yield one + f

def _digit_count(n):
	return len(str(n))

def _dcn_gt_dcd(f):
	return _digit_count(f.numerator) > _digit_count(f.denominator)

if __name__=="__main__":
	print(len(list(filter(_dcn_gt_dcd, gen_sqrt_2_terms(1000)))))

