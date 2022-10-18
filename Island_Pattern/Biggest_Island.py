from collections import deque
class Solution1:
    def Islands(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        biggest = 0


        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    biggest = max(biggest, self.IslandsDFS(matrix, i, j))

        return biggest


    def IslandsDFS(self, matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return

        if matrix[i][j] == 0:
            return

        area = 1

        area += self.IslandsDFS(matrix, i + 1, j)
        area += self.IslandsDFS(matrix, i - 1, j)
        area += self.IslandsDFS(matrix, i, j + 1)
        area += self.IslandsDFS(matrix, i, j - 1)

        return area


class Solution2:
    def Islands(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        biggest = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    biggest = max(biggest, self.IslandsBFS(matrix, i, j))

        return biggest

    def IslandsBFS(self, matrix, x, y):
        queue = deque([x, y])
        area = 0
        while queue:

            row, col = queue.popleft()

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue

            if matrix[row][col] == 0:
                continue

            area += 1

            queue.extend([row + 1, col])
            queue.extend([row - 1, col])
            queue.extend([row, col + 1])
            queue.extend([row, col - 1])

            return area
