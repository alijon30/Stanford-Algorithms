class Solution:


    def Islands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visited_islands = [[False for j in range(cols)] for i in range(rows)]
        islandSet = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and not visited_islands[i][j]:
                    traversal = self.IslandTraversal(matrix, visited_islands, i, j, "O")
                    islandSet.add(traversal)

        return islandSet


    def IslandTraversal(self, matrix, visited_islands, x, y, direction):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return ""

        if matrix[x][y] == 0 or visited_islands[x][y]:
            return ""

        visited_islands[x][y] = True

        islandTraversal = direction

        islandTraversal += self.IslandTraversal(matrix, visited_islands, x + 1, y, "D")
        islandTraversal += self.IslandTraversal(matrix, visited_islands, x - 1, y, "U")
        islandTraversal += self.IslandTraversal(matrix, visited_islands, x, y + 1, "R")
        islandTraversal += self.IslandTraversal(matrix, visited_islands, x, y - 1, "L")

        islandTraversal += "B"
        return islandTraversal