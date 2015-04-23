#!python
"""
Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.

				
			
			
			
			
		
		
		
		
		
		
	
	
	
	
 
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
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

mixed = partial(tile_holder, [1,2,3,4])

print(tile_len(50, mixed))
