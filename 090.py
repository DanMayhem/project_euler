#!python
"""
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""

from itertools import product, combinations

possible_faces = "0 1 2 3 4 5 6 7 8 9".split()
squares = "01 04 06 16 25 36 46 64 81".split()

def can_generate_square(s, d1, d2):
	i = s[0]
	j = s[1]
	if '9' in d1:
		d1 = d1 + ('6',)
	if '9' in d2:
		d2 = d2 + ('6',)
	if (i in d1) and (j in d2):
		return True
	if (i in d2) and (j in d1):
		return True
	return False

def can_generate_all_squares(d1, d2):
	for s in squares:
		if not can_generate_square(s, d1, d2):
			return False
	return True

results = []

for d1, d2 in product(combinations(possible_faces, 6), combinations(possible_faces, 6)):
	if can_generate_all_squares(d1, d2):
		if [d1, d2] not in results and [d2, d1] not in results:
			results.append([d1, d2])
			print([d1,d2])
print(len(results))