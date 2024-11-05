class Node:
    def __init__(self, key, left= None, right= None):
        self.key = key
        self.left = left
        self.right = right

class Splay:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.root = self._insert(key, self.root)
        self.root = self.splay(key, self.root)
        
    def _insert(self, key, node):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(key, node.left)
        elif key > node.key:
            node.right = self._insert(key, node.right)
        return node
            
    def splay(self, key, node):
        if not node or key == node.key:
            return node
        if key < node.key:
            if not node.left:
                return node
            if key < node.left.key:
                node.left.left = self.splay(key, node.left.left)
            elif key > node.right.key:
                node.left.right = self.splay(key, node.left.right)
            if node.left:
                node = self.rotate_right(node)
            return node if not node.left else self.rotate_right(node)
            
        elif key > node.key:
            if not node.right:
                return node
            if key < node.right.key:
                node.right.left = self.splay(key, node.right.left)
            elif key > node.right.key:
                node.right.right = self.splay(key, node.right.right)
            if node.right:
                node = self.rotate_left(node)
            return node if not node.right else self.rotate_left(node)
            
    def rotate_right(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        return y
        
    def rotate_left(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        return y
        
    def delete(self, key):
        self.root = self._delete(key, self.root)
        
    def _delete(self, key, node):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right =  self._delete(key, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self.findmin(node.right)
                node.key = temp.key
                node.right = self._delete(temp.key, node.right)
        return node
        
    def findmin(self, node):
        c = node
        while c.left:
            c = c.left
        return c
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end= ' ')
            self.inorder(node.right)
        
if __name__ == '__main__':
    b = Splay()
    b.insert(10)
    b.insert(14)
    b.insert(7)
    b.inorder(b.root)
    b.insert(35)
    b.insert(40)
    print()
    b.inorder(b.root)
    b.delete(10)
    b.delete(40)
    print()
    b.inorder(b.root)
    
    
            
                
            
            
        