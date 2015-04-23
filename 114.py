#!python
"""
A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one black square. There are exactly seventeen ways of doing this.

						
				
				
				
				
				
		
			
			
			
			
		
		
		
	
	

 
How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), black (1), and red (4).
"""

from functools import lru_cache

min_block = 3
max_block = 2

@lru_cache(maxsize=None)
def fill_row_count(row_len):
	print(row_len)
	count = 1
	if min_block > row_len:
		return count
	for block_len in range(min_block, row_len+1):
		for pos in range(0, row_len - block_len+1):
			count += fill_row_count(pos-1)
	return count


print(fill_row_count(50))