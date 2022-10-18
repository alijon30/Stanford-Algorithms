class Solution:


    def Islands(self,matrix):
        rows = len(matrix)
        col = len(matrix[0])
        islands_visited = [[False for i in range(col)] for j in range(rows)]
        CountClosedIslands = 0


        for i in range(rows):
            for j in range(col):
                if matrix[i][j] == 1:
                    if self.ClosedIslands(matrix, islands_visited, i, j):
                        CountClosedIslands += 1

        return CountClosedIslands


    def ClosedIslands(self, matrix, visited_islands, x, y):

        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return False

        if matrix[x][y] == 0 or visited_islands[x][y]:
            return False

        visited_islands[x][y] = True

        is_closed = True

        is_closed = self.ClosedIslands(matrix, visited_islands, x+ 1, y)
        is_closed = self.ClosedIslands(matrix, visited_islands, x- 1, y)
        is_closed = self.ClosedIslands(matrix, visited_islands, x, y + 1)
        is_closed = self.ClosedIslands(matrix, visited_islands, x, y - 1)

        return is_closed