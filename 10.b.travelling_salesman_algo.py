def tsp_branch_and_bound(graph):
    
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    visited = {vertex: False for vertex in vertices}
    visited[vertices[0]] = True

    min_cost = [float('inf')] 

    def calculate_path_cost(path):
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]
        cost += graph[path[-1]][path[0]]
        return cost

    def tsp_util(curr_vertex, visited, path, cost, min_cost):
        if len(path) == num_vertices:  
            total_cost = calculate_path_cost(path) 
            if total_cost < min_cost[0]: 
                min_cost[0] = total_cost
            return

        for neighbor, weight in graph[curr_vertex].items():
            if not visited[neighbor]:  
                visited[neighbor] = True  
                path.append(neighbor)  
                tsp_util(neighbor, visited, path, cost + weight, min_cost)  
                path.pop()  
                visited[neighbor] = False  

    tsp_util(vertices[0], visited, [vertices[0]], 0, min_cost)

    return min_cost[0] 

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

min_cost = tsp_branch_and_bound(graph)
print("Minimum cost:", min_cost)