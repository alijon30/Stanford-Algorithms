class Solution:
    def Perimter(self, matrix):
        row = len(matrix)
        cols = len(matrix[0])
        visited_islands = [[False for i in range(cols)]for j in range(row)]

        for i in range(row):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited_islands[i][j]:
                    return self.PerimeterHelper(matrix, visited_islands, i, j)


    def PerimeterHelper(self, matrix, visited_islands, x, y):
        if x < 0 or x>= len(matrix) or y < 0 or y >= len(matrix[0]):
            return 1 # returning 1, since this is a boundary cell

        if matrix[x][y] == 0:
            return 1

        if visited_islands[x][y]:
            return 0

        visited_islands[x][y] = True

        edgeCount = 0

        edgeCount += self.PerimeterHelper(matrix, visited_islands, x + 1, y)
        edgeCount += self.PerimeterHelper(matrix, visited_islands, x - 1, y)
        edgeCount += self.PerimeterHelper(matrix, visited_islands, x, y + 1)
        edgeCount += self.PerimeterHelper(matrix, visited_islands, x, y - 1)

        return edgeCount