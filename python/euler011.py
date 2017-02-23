def maxProdAdj(grid, row, col):
	currentMax = 0
	size = len(grid)
	if row < size - 3: #down
		product = grid[row][col] * grid[row+1][col] * grid[row+2][col] * grid[row+3][col]
		currentMax = max(currentMax, product)
	if  row < size - 3 and col > 2: #down left
		product = grid[row][col] * grid[row+1][col-1] * grid[row+2][col-2] * grid[row+3][col-3]
		currentMax = max(currentMax, product)
	if  row < size - 3 and col < size - 3: #down right
		product = grid[row][col] * grid[row+1][col+1] * grid[row+2][col+2] * grid[row+3][col+3]
		currentMax = max(currentMax, product)
	if  col < size - 3: #right
		product = grid[row][col] * grid[row][col+1] * grid[row][col+2] * grid[row][col+3]
		currentMax = max(currentMax, product)
	return currentMax

grid = []

file = open("../fixtures/euler011")
for line in file:
	grid.append([int(n) for n in line.split()])

currentMax = 0

for i in range(0, len(grid) - 4):
	for j in range(0, len(grid[0])):
		currentMax = max(currentMax, maxProdAdj(grid, i, j))

print currentMax