class Solution:

    def FloodFill(self, matrix, x, y, newColor):

        if matrix[x][y] != newColor:
            self.FillDFS(matrix, x, y, matrix[x][y], newColor)

        return matrix

    def FillDFS(self, matrix, x, y, oldColor, newColor):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return

        if matrix[x][y] != oldColor:
            return

        matrix[x][y] = newColor

        self.FillDFS(matrix, x + 1, y, oldColor, newColor)
        self.FillDFS(matrix, x - 1, y, oldColor, newColor)
        self.FillDFS(matrix, x, y + 1, oldColor, newColor)
        self.FillDFS(matrix, x, y-1, oldColor, newColor)