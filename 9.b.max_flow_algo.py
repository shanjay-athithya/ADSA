def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    visited[source] = True
    queue = [source]
    
    while queue:
        u = queue.pop(0)
        for v, cap in enumerate(graph[u]):
            if cap > 0 and not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sink]
    
def ford(graph, source, sink):
    max = 0
    parent = [-1]* len(graph)
    
    while bfs(graph, source, sink, parent):
        flow = float("inf")
        s = sink
        while s!= source:
            flow = min(flow, graph[parent[s]][s])
            s = parent[s]  
             
        max += flow
        
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= flow
            graph[v][u] += flow
            v = parent[v]
            
    return max
    
if __name__ == '__main__':
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    source = 0
    sink = 5
    print("Maximum flow:", ford(graph, source, sink))
            