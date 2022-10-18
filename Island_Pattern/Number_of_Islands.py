from collections import deque
class Solution1:

    def Islands(self, matrix):

        rows = len(matrix)
        colomuns = len(matrix[0])
        total_islands = 0

        for i in range(rows):
            for j in range(colomuns):
                if matrix[i][j] == 1:
                    total_islands += 1
                    self.IslandsDFS(matrix, i, j)

        return total_islands


    def IslandsDFS(self, matrix, x, y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return

        if matrix[x][y] == 0:
            return

        matrix[x][y] = 0

        self.IslandsDFS(matrix, x+1, y)
        self.IslandsDFS(matrix, x- 1, y)
        self.IslandsDFS(matrix, x, y+ 1)
        self.IslandsDFS(matrix, x, y-1)


class Solution2:
    def Islands(self, matrix):
        rows = len(matrix)
        colomuns = len(matrix[0])
        totalIslands = 0


        for i in range(rows):
            for j in range(colomuns):
                if matrix[i][j] == 1:
                    totalIslands += 1
                    self.IslandsBFS(matrix, i, j)

        return totalIslands

    def IslandsBFS(self, matrix, x, y):
        queue = deque([x, y])

        while queue:
            row, colomun = queue.popleft()

            if row < 0 or row >= len(matrix) or colomun < 0 or colomun >= len(matrix[0]):
                continue

            if matrix[row][colomun] == 0:
                continue

            matrix[row][colomun] = 0

            queue.extend([row + 1, colomun])
            queue.extend([row - 1, colomun])
            queue.extend([row, colomun + 1])
            queue.extend([row, colomun - 1])


class Solution3:
    def Islands(self, matrix):
        rows = len(matrix)
        colomuns = len(matrix[0])
        totalIslands = 0
        visited = [[False for i in range(colomuns)] for j in range(rows)]


        for i in range(rows):
            for j in range(colomuns):
                if matrix[i][j] == 1 and not visited[i][j]:
                    totalIslands += 1
                    self.IslandsBFS(matrix,visited, i, j)

        return totalIslands

    def IslandsBFS(self, matrix, visited, x, y):
        queue = deque([x, y])

        while queue:
            row, col = queue.popleft()

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue

            if matrix[row][col]  == 0 or visited[row][col]:
                continue
            
            visited[row][col] = True

            queue.extend([row + 1, col])
            queue.extend([row -1, col])
            queue.extend([row, col + 1])
            queue.extend([row, col - 1])