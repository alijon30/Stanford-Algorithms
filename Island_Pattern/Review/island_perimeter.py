

def findIslandPerimeter(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)]for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                return IslandPermiterDFS(matrix, i, j, visited)

    return 0
def IslandPermiterDFS(matrix, x, y, visited):

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 1

    if matrix[x][y] == 0:
        return 1

    if visited[x][y]:
        return 0

    visited[x][y] = True

    edgeCount = 0

    edgeCount+= IslandPermiterDFS(matrix, x+1, y, visited)
    edgeCount += IslandPermiterDFS(matrix, x -1, y, visited)
    edgeCount += IslandPermiterDFS(matrix, x , y+1, visited)
    edgeCount += IslandPermiterDFS(matrix, x, y-1, visited)

    return edgeCount

def main():
    print(findIslandPerimeter([[1, 1, 0, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 1, 0, 0, 0],
                               [0, 1, 1, 0, 0],
                               [0, 0, 0, 0, 0]]))

    print(findIslandPerimeter([[0, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 1, 0, 0],
                               [0, 1, 1, 0],
                               [0, 1, 0, 0]]))


main()

