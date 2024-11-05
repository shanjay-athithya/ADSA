def dfs(graph,start):
    stack=[start]
    visited=[]
    while stack:
        v=stack.pop()
        if v not in visited:
            visited.append(v)
            stack.extend(i for i in graph[v] if i not in visited)
            print(v)
    print(visited)
            
def bfs(graph,start):
    queue=[start]
    visited=[]
    while queue:
        v=queue.pop(0)
        if v not in visited:
            visited.append(v)
            queue.extend(i for i in graph[v] if i not in visited)
            print(v)
            
def idfs(graph, start, depth):
    stack = [(start, 0)]
    visited = []
    while stack:
        v, current_depth = stack.pop()
        if v not in visited:
            visited.append(v)
            if current_depth < depth:
                stack.extend((i, current_depth + 1) for i in graph[v] if i not in visited)
            print(v)
def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth {depth}:")
        idfs(graph, start, depth)
            
if __name__ == '__main__':       
    graph={
        '0':['1','2'],
        '1':['2'],
        '2':['1']
    }
    print("bfs")
    bfs(graph, "0")
    print("dfs")
    dfs(graph,'0')
    print("iterative deepening")
    iddfs(graph, '0', 3)