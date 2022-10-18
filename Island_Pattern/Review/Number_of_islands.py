
from collections import deque


def countIslandsDFS(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                totalIslands += 1
                visitedBFS(matrix, i, j)

    return totalIslands

def visitedDFS(matrix, x, y):

    if x < 0 or x >= len(matrix) or y <0 or y >= len(matrix[0]):
        return

    if matrix[x][y] == 0:
        return

    matrix[x][y] = 0

    visitedDFS(matrix, x+1, y) #lower cell
    visitedDFS(matrix, x-1, y) #upper cell
    visitedDFS(matrix, x, y+ 1) #right cell
    visitedDFS(matrix, x, y-1) # left cell

def visitedBFS(matrix, x, y):
    neighbors = deque([(x,y)])
    while neighbors:
        row, col = neighbors.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue
        if matrix[row][col] == 0:
            continue
        matrix[row][col] = 0

        neighbors.extend([(row+1, col)])
        neighbors.extend([(row-1, col)])
        neighbors.extend([(row, col+1)])
        neighbors.extend([(row, col-1)])
def main():
    print(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
        0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
        0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))

main()


#Solution 3
def findIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0
    visited = [[False for x in range(cols) ]for y in range(rows)]

    for i in range(rows):
        for j in range(len(cols)):
            if matrix[rows][cols] == 1 and not visited[rows][cols] :
                totalIslands += 1
                visitedIslandsBFS(matrix, i, j, visited)

    return totalIslands

def visitedIslandsBFS(matrix, x, y, visited):
    queue = deque([(x, y)])
    while queue:
        row, col = queue.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue

        if matrix[row][col] == 0 or visited[row][col]:
            continue

        visited[row][col] = True

        queue.extend([(row + 1, col)])
        queue.extend([(row-1, col)])
        queue.extend([(row, col+1)])
        queue.extend([(row, col-1)])
        
