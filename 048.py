#!python
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""



if __name__=="__main__":
	n = 1000
	print(str(sum([(i+1)**(i+1) for i in range(n)]))[-10:])
