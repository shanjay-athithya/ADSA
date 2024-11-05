"""string = 'ABCDAAADB'
fre = {}
for i in string:
    fre[i] = string.count(i)
    
temp = sorted(fre.items(), key= lambda x: x[1])

class Node:
    def __init__(self, right, left):
        self.right = right  
        self.left = left
        
    def children(self):
        return (self.right, self.left)

while len(temp) > 1:
    left, right = temp[0], temp[1]
    n = Node(left[0], right[0])
    temp.append((n, left[1]+right[1]))
    temp = temp[2:]
    temp = sorted(temp, key=lambda x: x[1])
    
def huffman(node, s = ''):
    if isinstance(node , str):
        return {node:s}
    if node is None:
        return {}
    d ={}
    d.update(huffman(node.left, s= s+'0'))
    d.update(huffman(node.right, s = s +'1'))
    return d
    
print(huffman(temp[0][0]))

for i, j in huffman(temp[0][0]).items():
    print(i, j)
    
    
import math
def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def short_distance_res(points):
    points.sort(key= lambda x: x[0])
    def short_distance(points):
        n = len(points)
        if n <= 3:
            min_dist = float('inf')
            close_points = None
            for i in range(n):
                for j in range(i+1, n):
                    dist = distance(points[i], points[j])
                    if dist < min_dist:
                        min_dist = dist
                        close_points = [points[i], points[j]]
            return min_dist
        
        mid = n//2
        left = points[:mid]
        right = points[mid:]
        
        l_dist, l_points = short_distance(left)
        r_dist, r_points = short_distance(right)
        
        min_dist = min(l_dist, r_dist)
        close_points = l_points if l_dist < min_dist else r_points
        
        strip = [p for p in points if abs(p[0] - points[mid][0]) < min_dist]
        
        strip.sort(key = lambda x: x[1])
        
        m = len(strip)
        
        for i in range(m):
            for j in range(i +1 , min(m, i + 8)):
                dist = distance(points[i], points[j])
                if dist < min_dist:
                    min_dist = dist
                    close_points = [points[i],points[j]]
                    
        return min_dist, close_points
    return short_distance(points)     
        
            
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_distance, closest_points = short_distance_res(points)
print("Closest distance:", min_distance)
print("Closest points:", closest_points)

def dfs(graph, start, end):
    visited = []
    stack = [start, [start]]
    while stack:
        node, path = stack.pop()
        if node == end:
            return path
        if node not in visited:
            visited.append(node)
            for i in graph[node]:
                stack.append(i, path + [i])

string = 'ABCAAAC'

fre = {}

for i in string:
    if i  not in fre:
        fre[i] = string.count(i)
        
temp = sorted(fre.items,key = lambda x: x[1])

while len(temp) > 1:
    right = temp[0]
    left = temp[1]
    n = Node(left, right)
    temp.append((n, left[1] + right[1]))
    temp[2:]
    temp.sort(key= lambda x:x[1])
    
def huffman(node, string = ''):
    if isinstance(node, string):
        return {node: string}
    if node is None:
        return {}
    d ={}
    d.update(huffman(node.left,  string = string + '0'))
    d.update(huffman(node.right, string = string +'1'))
    return d

print(huffman(temp[0][0]))
a = huffman(temp[0][0])
encode = ''.join(a[s] for s in string)

def decode(encode, tree):
    string = encode
    current = tree
    s= ''
    for bit in string:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if isinstance(current, string):
            s += current
            current= tree       
    return s
  
  
class FindUnion():
    def __init__(self, n):
        self.parents = list(range(n))     
        
    def find(self, x):
        if self.parents[x] !=  x:
            self.parent[x] = self.find(self.parents[x])
            
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)
        
        
def kurshals(graph, n):
    mst = []
    fu = FindUnion(n)
    for u, v , weight in graph:
        if fu.find(u) != fu.find(v):
            mst.append((u, v, weight))
            fu.union(u, v)
    return mst"""
    
class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.next_leaf = None  # Pointer to the next leaf node (for leaf nodes only)
        
    def add_key(self, key, child=None):
        if child:
            self.keys.append(key)
            self.children.append(child)
        else:
            self.keys.append(key)
            
    def is_full(self, m):
        return len(self.keys) >= m
    
    def split(self, m):
        mid_index = len(self.keys) // 2
        new_node = BPlusTreeNode(is_leaf=self.is_leaf)
        new_node.keys = self.keys[mid_index:]
        new_node.children = self.children[mid_index:]
        self.keys = self.keys[:mid_index]
        self.children = self.children[:mid_index]
        return new_node


class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node.is_leaf:
            for i in range(len(node.keys)):
                if node.keys[i] == key:
                    return True
            return False
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self._search_recursive(node.children[i], key)
    
    def insert(self, key):
        self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if node.is_leaf:
            node.add_key(key)
            if node.is_full(self.order):
                self._split_leaf(node)
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            self._insert_recursive(node.children[i], key)
    
    def _split_leaf(self, leaf_node):
        new_leaf = leaf_node.split(self.order)
        new_leaf.next_leaf = leaf_node.next_leaf
        leaf_node.next_leaf = new_leaf
    
    def delete(self, key):
        return self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        if node.is_leaf:
            if key in node.keys:
                node.keys.remove(key)
                return True
            return False
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self._delete_recursive(node.children[i], key)
        
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        result = []
        if node:
            if node.is_leaf:
                for key in node.keys:
                    result.append(key)
            else:
                for i in range(len(node.keys)):
                    result += self._inorder_recursive(node.children[i])
                    result.append(node.keys[i])
                result += self._inorder_recursive(node.children[-1])
        return result


# Example usage
bplus_tree = BPlusTree(order=4)
keys_to_insert = [10, 20, 5, 30, 15, 25]

for key in keys_to_insert:
    bplus_tree.insert(key)

print("Search for key 20:", bplus_tree.search(20))  # Output: True
print("Search for key 50:", bplus_tree.search(50))  # Output: False

bplus_tree.delete(20)
print("Search for key 20 after deletion:", bplus_tree.search(20))  # Output: False