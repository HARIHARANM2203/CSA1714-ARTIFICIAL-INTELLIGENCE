
# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Depth Limited Search
def dls(node, goal, limit, path):
    if node == goal:
        return path

    if limit <= 0:
        return None

    for neighbor in graph[node]:
        if neighbor not in path:
            result = dls(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None

# Iterative Deepening DFS
def iddfs(start, goal):
    for depth in range(len(graph)):
        result = dls(start, goal, depth, [start])

        if result:
            return result

    return None

# Main program
start = 'A'
goal = 'G'

path = iddfs(start, goal)

if path:
    print("Path Found:", path)
else:
    print("Goal Not Found")
