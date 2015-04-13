#!python
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from functools import partial

cubes = [ i**3 for i in range(1,10000)]

def is_permutation(x, l):
	return str(sorted(list(str(x)))) == str(sorted(list(str(l))))

if __name__=="__main__":
	m = 5
	for i in range(len(cubes)):
		c=cubes[i]
		if len(list(filter(partial(is_permutation, c), cubes[i:])))==m:
			print(c)
			exit()
