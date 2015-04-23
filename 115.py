#!python
"""
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length of m units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function first exceeds one million.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fill_row_count(min_block, row_len):
	count = 1
	if min_block > row_len:
		return count
	for block_len in range(min_block, row_len+1):
		for pos in range(0, row_len - block_len+1):
			count += fill_row_count(min_block, pos-1)
	return count

target = 1000000

m=50
f=0
n=m
while f < target:
	f = fill_row_count(m,n)
	print([m,n,f])
	n+=1
