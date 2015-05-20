#!python
"""
In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid as indicated in the sketch.


There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles could be situated within those smaller grids:

1x1: 1 
2x1: 4 
3x1: 8 
1x2: 4 
2x2: 18

Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?
"""

from itertools import combinations, product
from functools import lru_cache
from pe import choose

c = 0

maxx = 47
maxy = 43

step = [None for i in range(maxx+1)]
last_step=-1
last_r=-1

def gen_lattice_points(a,b,c,d):
	#assume a and b are parallel and c and d are parellel
	#the sign of each value is the slope of the line, the value is the y intercept
	#y0=m0x0+0
	#y1=m1x1+b1
	#a,c
	yield (a+c)/2,(c-a)/2
	#a,d
	yield (a+d)/2,(d-a)/2
	#b,c
	yield (b+c)/2,(c-b)/2
	#b,d
	yield (b+d)/2,(d-b)/2

def gen_lattice_points_c(a,b,c,d):
	return list(gen_lattice_points(a,b,c,d))


def is_sub_rect_in_rect(a,b,c,d,x,y):
	for i, j in gen_lattice_points(a,b,c,d):
		if (i<0) or (i>x) or (j<0) or (j>y):
			return False
	return True

@lru_cache(maxsize=None)
def calc_diag_grids(x,y):
	global last_r, last_step, step
	if x > y:
		return calc_diag_grids(y,x)
	if step[x] is not None:
		r = last_r+step[x]
		last_r = r
		return r
	m = max((x,y))
	b1 = list(range(-2*m,2*m))
	b2 = list(range(-2*m,2*m))
	r = 0
	for a,b in combinations(b1,2):
		for c,d in combinations(b2,2):
			if is_sub_rect_in_rect(a,b,c,d,x,y):
				r+=1
	if r-last_r==last_step:
		step[x]=last_step
	last_step = r-last_r
	last_r=r
	return r


for i in range(1,maxy+1):
	for j in range(1,maxx+1):
		c1 = choose(i+1,2)*choose(j+1,2)
		c2 = calc_diag_grids(i,j)
		c+=c1+c2
		print("{0}x{1}: {2} ({3}+{4}) => {5}".format(i,j,c1+c2,c1,c2,c))
print(c)