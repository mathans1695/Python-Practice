from life import LifeGrid

INIT_CONFIG = [(0,0), (0,1), (1,0), (1,2), (3,2), (3,4), (5,4), (5,6), (7,6), (7,8), (9,8), (9,10), (11,10), (11, 12), (12, 11), (12,12)]

GRID_WIDTH = int(input("Enter grid width: "))
GRID_HEIGHT = int(input("Enter grid height: "))

NUM_GENS = int(input("Enter the num of generations: "))

def main():
	
	grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
	grid.configure(INIT_CONFIG)
	
	draw(grid)
	for i in range(NUM_GENS):
		evolve(grid)
		draw(grid)
		
def evolve(grid):
	liveCells = list()
	
	for i in range(grid.numRows()):
		for j in range(grid.numCols()):
			
			neighbors = grid.numLiveNeighbors(i, j)
			
			if (neighbors == 2 and grid.isLiveCell(i, j)) or \
			   (neighbors == 3):
				liveCells.append((i, j))
	
	grid.configure(liveCells)
	
def draw(grid):
	for i in range(GRID_WIDTH):
		for j in range(GRID_HEIGHT):
			print(grid._grid[i, j], end = "")
		print()
	print()
	
main()