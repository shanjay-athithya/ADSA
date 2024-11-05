def safe(graph, path, vertex, pos):
    if graph[path[pos-1]][vertex] == 0:
        return  False
    if vertex in path:
        return False
    return True
    
def check(graph, path, pos):
    n = len(graph)
    if pos == n:
        return graph[path[pos-1]][path[0]] == 1
      
    for vertex in range(0, n):
        if safe(graph, path, vertex, pos):
            path[pos] = vertex
            if check(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False
    
def hamiltonian(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0
    if not check(graph, path, 1):
        print("not exists")
        
    print(" -> ".join(map(str, path + [0])))
    
graph = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ]

hamiltonian(graph)
            