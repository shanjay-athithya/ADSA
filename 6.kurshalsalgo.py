class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    mst = []
    union_find = UnionFind(n)

    for u, v, weight in edges:
        if union_find.find(u) != union_find.find(v):
            mst.append((u, v, weight))
            union_find.union(u, v)

    return mst

if __name__ == "__main__":
    vertex_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 3), ('B', 'D', 5), ('B', 'E', 1),
        ('C', 'E', 4),
        ('D', 'E', 7)
    ]

    # Convert letters to numerical indices using the vertex map
    edges_numeric = [(vertex_map[u], vertex_map[v], weight) for u, v, weight in edges]
    n = len(edges_numeric)  # Number of vertices
    mst = kruskal(edges_numeric, n)
    print("Minimum Spanning Tree (MST):", mst)
