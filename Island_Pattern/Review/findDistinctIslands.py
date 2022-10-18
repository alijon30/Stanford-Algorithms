


def findDistinctIslands(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False for x in range(cols)]for y in range(rows)]

    sets = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                returned = findDFS(matrix, i, j, visited, "O")
                sets.add(returned)

    print(sets)
    return len(sets)


def findDFS(matrix, x, y, visited, origin):

    if x < 0 or x>= len(matrix) or y < 0 or y >= len(matrix[0]):
        return ""

    if matrix[x][y] == 0 or visited[x][y]:
        return ""

    visited[x][y] = True

    edge = origin

    edge += findDFS(matrix, x+1, y, visited, "D")
    edge += findDFS(matrix, x-1, y, visited, "U")
    edge += findDFS(matrix, x, y+1, visited, "R")
    edge += findDFS(matrix, x, y-1, visited, "L")

    edge += "B"
    return edge


def main():
    print(findDistinctIslands([[1, 1, 0, 1, 1],
                               [1, 1, 0, 1, 1],
                               [0, 0, 0, 0, 0],
                               [0, 1, 1, 0, 1],
                               [0, 1, 1, 0, 1]]))

    print(findDistinctIslands([[1, 1, 0, 1],
                               [0, 1, 1, 0],
                               [0, 0, 0, 0],
                               [1, 1, 0, 0],
                               [0, 1, 1, 0]]))


main()