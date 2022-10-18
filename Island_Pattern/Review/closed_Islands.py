

def countClosedIslandsDFS(matrix):

    closed_islands = 0

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False for x in range(cols)] for y in range(rows)]


    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                if countDFS(matrix, i, j, visited):
                    closed_islands += 1

    return closed_islands

def countDFS(matrix, x, y, visited):

    if x < 0 or x >=len(matrix) or y <0 or y >= len(matrix[0]):
        return  False

    if matrix[x][y] == 0 or  visited[x][y]:
        return True

    visited[x][y] = True

    is_island = True

    is_island &= countDFS(matrix, x-1, y, visited)
    is_island &= countDFS(matrix, x +1, y, visited)
    is_island &= countDFS(matrix, x, y+1, visited)
    is_island &= countDFS(matrix, x, y-1, visited)

    return is_island

def main():
    print(countClosedIslandsDFS([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))

    print(countClosedIslandsDFS([[0, 0, 0, 0], [0, 1, 0, 0], [
          0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))


main()


