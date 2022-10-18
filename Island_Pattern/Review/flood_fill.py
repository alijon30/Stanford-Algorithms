


def floodFill(matrix, x, y, newColor):

    if matrix[x][y] != newColor:
        fillDFS(matrix, x, y, matrix[x][y], newColor)

    return matrix


def fillDFS(matrix, x, y, oldColor, newColor):

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return

    if matrix[x][y] != oldColor:
        return

    matrix[x][y] = newColor

    fillDFS(matrix, x+1, y, oldColor, newColor)
    fillDFS(matrix, x-1, y, oldColor, newColor)
    fillDFS(matrix, x, y+1, oldColor, newColor)
    fillDFS(matrix, x, y-1, oldColor, newColor)

def main():
    print(floodFill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))
    print(floodFill([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


main()