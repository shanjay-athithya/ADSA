def tsp(graph, source):
    n = len(graph)
    visited = [False] * n
    visited[source] = True
    tour = [source]
    for i in range(n - 1):
        mind = float('inf')
        current = tour[-1]
        near = None
        for next in range(n):
            if not visited[next] and mind > graph[current][next]:
                mind = graph[current][next]
                near = next
        visited[near] = True
        tour.append(near)
    tour.append(source)
    dist = sum(graph[tour[i]][tour[i + 1]] for i in range(n))
    
    return tour, dist
if __name__ == '__main__':
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tour, a =tsp(graph, 0)

    print("Tour:", (tour, a))
                
 
