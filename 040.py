#!python
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def champernownes_nth_digit(n):
	pos = 0 #start at position 1
	i = 0 #the integer value at pos
	e = 0
	while pos < n:
		#jump ahead one order of magnitude
		e += 1
		i = 10**e
		pos += e*10**e
	#oops we went too far back off one order of magnitude
	pos -= e*10**e
	i = 10**(e-1)
	#how we can move through by an integers width until we go too far
	#e tells how many digits are in th enumbers in this range
	while pos <= n:
		pos += e
		i += 1
	#oops we wen too far, back off by one integer
	i -= 2
	pos -= e
	return int(str(i)[pos-n])

def cnd(n):
	i=1
	s = str(i)
	while len(s) < n:
		i+=1
		s += str(i)
	return int(s[n-1])

if __name__=="__main__":
	p = 1
	for e in range(7):
		p*= cnd(10**e)
	print(p)
