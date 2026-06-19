# Function to check if it is safe to assign a color to a node
def isSafe(node, color, graph, n, col):
    for k in range(n):
        # Check if adjacent node has the same color
        if k != node and graph[k][node] == 1 and color[k] == col:
            return False
    return True  # Safe to assign the color

# Recursive function to solve the coloring problem


def solve(node, color, m, N, graph):
    # If all nodes are assigned colors, return True
    if node == N:
        return True 

    # Try different colors for the node
    for i in range(1, m + 1):
        if isSafe(node, color, graph, N, i):
            color[node] = i
            # Recursively check for the next node
            if solve(node + 1, color, m, N, graph):
                return True
            color[node] = 0  # Backtrack if the color assignment fails
    return False  # If no solution is found

# Function to check if graph can be colored with m colors

def graphColoring(graph, m, N):
    color = [0] * N
    # Start solving from node 0
    if solve(0, color, m, N, graph):
        return True
    return False


# Driver code
if __name__ == "__main__":
    N = 4  # Number of nodes
    m = 3  # Maximum number of colors

    # Create a sample graph with edges (0,1), (1,2), (2,3), (3,0), (0,2)
    graph = [[False] * 101 for _ in range(101)]
    graph[0][1] = graph[1][0] = True
    graph[1][2] = graph[2][1] = True
    graph[2][3] = graph[3][2] = True
    graph[3][0] = graph[0][3] = True
    graph[0][2] = graph[2][0] = True

    # Output if the graph can be colored with at most m colors
    print(graphColoring(graph, m, N))
