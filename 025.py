#!python
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fib(max=None):
	a = 0
	b = 1
	while (max is None) or (b < max):
		yield b
		c = a + b
		a = b
		b = c

if __name__=="__main__":
	i = 0
	for n in fib():
		i+=1
		if len(str(n)) >= 1000:
			print(i)
			exit()
