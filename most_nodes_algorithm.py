def find_best_path(filename: str):
    # Read input from file
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    time_limit = 0
    start_node = 0
    matrix = []
    
    # Parse lines for time, start, and matrix
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("Defined Time"):
            time_limit = int(line.split(":")[1].strip())
        elif line.startswith("Which node"):
            start_node = int(line.split(":")[1].strip())
            # Skip header line of matrix
            i += 1
        else:
            parts = lines[i].split()
            if parts and parts[0].isdigit():
                # Convert row (skip the first index token)
                row = [int(x) for x in parts[1:]]
                matrix.append(row)
        i += 1
        
        
    n = len(matrix)
    # Build adjacency list: graph[node] = list of (neighbor, cost)
    graph = {u: [] for u in range(1, n+1)}
    for u in range(1, n+1):
        for v in range(1, n+1):
            cost = matrix[u-1][v-1]
            if cost > 0:
                graph[u].append((v, cost))
    
    # Variables to track the best path
    best_path = []
    best_cost = 0
    best_count = 0
    
    visited = [False] * (n+1)
    visited[start_node] = True
    path = [start_node]
    
    # DFS function
    def dfs(node, current_cost):
        nonlocal best_path, best_cost, best_count
        # Update best if this path visits more nodes
        if len(path) > best_count:
            best_count = len(path)
            best_path = list(path)
            best_cost = current_cost
        elif len(path) == best_count and current_cost < best_cost:
            # Optionally prefer smaller cost for ties
            best_path = list(path)
            best_cost = current_cost
        
        # Explore neighbors recursively
        for (nbr, w) in graph[node]:
            if not visited[nbr] and current_cost + w <= time_limit:
                visited[nbr] = True
                path.append(nbr)
                dfs(nbr, current_cost + w)
                # Backtrack
                path.pop()
                visited[nbr] = False
    
    
    # Start DFS from the start node
    dfs(start_node, 0)
    
    # Print the best path and cost (time used)
    print("Best path (max vertices):", best_path)
    print("Number of vertices visited:", best_count)
    print("Total time cost:", best_cost)

find_best_path("graph_values.txt")

input("\nPress Enter to close window...")
