
class Solution:

    def Islands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited_islands = [[False for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if not visited_islands[i][j]:
                    if self.ContainCycle(matrix, visited_islands, matrix[i][j], -1, -1):
                        return True

        return False


    def ContainCycle(self, matrix, visited_islands, startChar, x, y, prevX, prevY ):

        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False

        if matrix[x][y] != startChar:
            return False

        if visited_islands[x][y]:
            return  True

        visited_islands[x][y] = True

        if (x + 1 != prevX and self.ContainCycle(matrix, visited_islands, startChar, x + 1, y, x, y)):
            return True
        if (x - 1 != prevX and self.ContainCycle(matrix, visited_islands, startChar, x- 1, y, x, y)):
            return True
        if (y + 1 != prevY and self.ContainCycle(matrix, visited_islands, startChar, x, y + 1, x, y)):
            return True
        if (y - 1 != prevY and self.ContainCycle(matrix, visited_islands, startChar, x, y - 1, x, y)):
            return True

        return False