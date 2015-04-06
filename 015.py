#!python
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

class GridWalker:
	def __init__(self, width, height):
		self.grid = [[None for i in range(width+1)] for j in range(height+1)]
		self.width = width
		self.height = height
	def _count_routes_from_pos(self, x, y):
		n = 0
		if x<self.width:
			n = n + self._count_routes_from_pos(x+1,y)
		if y<self.height:
			n = n + self._count_routes_from_pos(x,y+1)
		if n == 0:
			n = 1
		return n

	def _routes_to_pos(self, x, y):
		if self.grid[x][y] is not None:
			return self.grid[x][y]
		self.grid[x][y] = 0
		if x>0:
			self.grid[x][y] += self._routes_to_pos(x-1,y)
		if y>0:
			self.grid[x][y] += self._routes_to_pos(x, y-1)
		return self.grid[x][y]

	def walk(self):
		#return self._count_routes_from_pos(0,0)
		self.grid[0][0]=1
		return self._routes_to_pos(self.width, self.height)

if __name__=="__main__":
	print(GridWalker(20,20).walk())