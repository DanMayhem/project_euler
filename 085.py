from pe import choose


limit = 1000

def num_rects(i, j):
	return choose(i+1, 2) * choose(j+1, 2)

print(num_rects(3,2))

mr = 999
target = 2000000

for i in range(1,limit):
	for j in range(1,i+1):
		nr = num_rects(i, j)
		if abs(target-nr) < mr:
			mr = target-nr
			print(i*j)


		