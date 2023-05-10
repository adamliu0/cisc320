def tsp(adj_matrix, start_node):
    n = len(adj_matrix)
    path = []
    visited = [False] * n
    visited[start_node] = True
    path.append(start_node)
    current = start_node
    dist = 0
    
    for i in range(n-1):
        next_node = -1
        min_dist = float('inf')
        for j in range(n):
            if not visited[j] and adj_matrix[current][j] < min_dist:
                next_node = j
                min_dist = adj_matrix[current][j]
        visited[next_node] = True
        path.append(next_node)
        dist += min_dist
        current = next_node
    
    dist += adj_matrix[path[-1]][start_node]
    path.append(start_node)
    return path, dist

# Reading the adjacency matrix from input.txt file
adj_matrix = []
with open('input.txt') as file:
    for line in file:
        adj_matrix.append([int(x) for x in line.split()])

start_node = 0 # Change this to any node you want to start at
path, dist = tsp(adj_matrix, start_node)
print(*path[:-1], sep="\n")
print(dist)
