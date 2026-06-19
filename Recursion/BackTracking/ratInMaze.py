class Solution:
    # Function to check if the cell is within maze and valid to move
    def isSafe(self, x, y, n, maze, visited):
        return (0 <= x < n and 0 <= y < n and
                maze[x][y] == 1 and visited[x][y] == 0)

    # Function to solve maze using backtracking
    def solve(self, x, y, n, maze, visited, path, res):

        # If destination reached, store the path
        if x == n - 1 and y == n - 1:
            res.append(path)
            return

        # Mark the cell visited
        visited[x][y] = 1

        # Try moving Down
        if self.isSafe(x + 1, y, n, maze, visited):
            self.solve(x + 1, y, n, maze, visited, path + "D", res)
        # Try moving Left
        if self.isSafe(x, y - 1, n, maze, visited):
            self.solve(x, y - 1, n, maze, visited, path + "L", res)
        # Try moving Right
        if self.isSafe(x, y + 1, n, maze, visited):
            self.solve(x, y + 1, n, maze, visited, path + "R", res)
        # Try moving Up
        if self.isSafe(x - 1, y, n, maze, visited):
            self.solve(x - 1, y, n, maze, visited, path + "U", res)

        # Backtrack: unmark cell as visited
        visited[x][y] = 0

    # Main function to find all paths
    def findPath(self, maze, n):
        res = []
        visited = [[0] * n for _ in range(n)]
        if maze[0][0] == 1:
            self.solve(0, 0, n, maze, visited, "", res)
        return res


# Driver code
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
n = len(maze)
obj = Solution()
paths = obj.findPath(maze, n)
print(" ".join(paths))
