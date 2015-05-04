#!python
"""
The minimum number of cubes to cover every visible face on a cuboid measuring 3 x 2 x 1 is twenty-two.


If we then add a second layer to this solid it would require forty-six cubes to cover every visible face, the third layer would require seventy-eight cubes, and the fourth layer would require one-hundred and eighteen cubes to cover every visible face.

However, the first layer on a cuboid measuring 5 x 1 x 1 also requires twenty-two cubes; similarly the first layer on cuboids measuring 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.

We shall define C(n) to represent the number of cuboids that contain n cubes in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.

It turns out that 154 is the least value of n for which C(n) = 10.

Find the least value of n for which C(n) = 1000.
"""

target = 1000
limit = 30000 #arbitrary

def blocks_for_cuboid_layer(x, y, z, n):
	return 2*(x*y+y*z+x*z)+4*(x+y+z+n-2)*(n-1)

C = [0 for i in range(limit)]

i = 1
while blocks_for_cuboid_layer(i,i,i,1) <= limit:
	j=i
	while blocks_for_cuboid_layer(i,j,i,1) <= limit:
		k=j
		while blocks_for_cuboid_layer(i,j,k,1) <= limit:
			n=1
			while blocks_for_cuboid_layer(i,j,k,n) < limit:
				C[blocks_for_cuboid_layer(i,j,k,n)] += 1
				n+=1
			k+=1
		j+=1
	i+=1

for i in range(limit):
	print([i, C[i]])
	if C[i] == target:
		exit()