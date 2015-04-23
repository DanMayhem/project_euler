#!python
"""
A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

			
			
			
			
		
		
		
 
If green tiles are chosen there are three ways.

		
		
		
 
And if blue tiles are chosen there are two ways.

	
	
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
"""

from functools import lru_cache, partial

@lru_cache(maxsize=None)
def tile_len(l, tiles):
	count = 0
	for t in tiles():
		if l == t:
			count += 1
		if l > t:
			count += tile_len(l-t, tiles)
	return count

def tile_holder(tiles):
	return tiles

red = partial(tile_holder, [1,2])
green = partial(tile_holder, [1,3])
blue = partial(tile_holder, [1,4])

print(tile_len(50, red)+tile_len(50,green)+tile_len(50,blue)-3)
