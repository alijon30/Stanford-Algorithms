from collections import deque

def maxAreaIslandDFS(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    biggest_island = 0

    current_length = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                current_length = findDFS(matrix, i, j)
                biggest_island = max(biggest_island, current_length)

    return biggest_island


def findDFS(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y>= len(matrix[0]):
        return 0

    if matrix[x][y] == 0:
        return 0

    matrix[x][y] = 0
    area = 1

    area += findDFS(matrix, x+1, y)
    area += findDFS(matrix, x-1, y)
    area += findDFS(matrix, x, y+1)
    area += findDFS(matrix, x, y-1)
    return area

def findBFS(matrix, x, y):
    queue = deque([(x, y)])
    area = 0
    while queue:
        row, col = queue.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue

        if matrix[row][col] == 0:
            continue

        matrix[row][col] = 0

        queue.extend([(row + 1, col)])
        queue.extend([(row-1, col)])
        queue.extend([(row, col+1)])
        queue.extend([(row, col-1)])
        

def main():
    print(maxAreaIslandDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()

