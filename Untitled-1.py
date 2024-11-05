class BPlusTreeNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.next_leaf = None  # Pointer to the next leaf node (for leaf nodes only)

    def is_full(self, order):
        return len(self.keys) >= order

    def split(self, order):
        mid_index = len(self.keys) // 2
        new_node = BPlusTreeNode(is_leaf=self.is_leaf)
        new_node.keys = self.keys[mid_index:]
        self.keys = self.keys[:mid_index]

        if not self.is_leaf:
            new_node.children = self.children[mid_index:]
            self.children = self.children[:mid_index]
        else:
            new_node.next_leaf = self.next_leaf
            self.next_leaf = new_node

        return new_node


class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode(is_leaf=True)
        self.order = order
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node.is_leaf:
            return key in node.keys
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self._search_recursive(node.children[i], key)
    
    def insert(self, key):
        root = self.root
        if root.is_full(self.order):
            new_root = BPlusTreeNode(is_leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)
    
    def _insert_non_full(self, node, key):
        if node.is_leaf:
            i = len(node.keys) - 1
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if node.children[i].is_full(self.order):
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)
    
    def _split_child(self, parent, index):
        order = self.order
        child = parent.children[index]
        new_child = child.split(order)
        parent.keys.insert(index, child.keys.pop())
        parent.children.insert(index + 1, new_child)
    
    def delete(self, key):
        self._delete_recursive(self.root, key)
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]
    
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
            if i < len(node.keys) and key == node.keys[i]:
                if self._delete_recursive(node.children[i + 1], key):
                    node.keys.pop(i)
                    return True
            elif self._delete_recursive(node.children[i], key):
                if len(node.children[i].keys) < self.order // 2:
                    self._balance(node, i)
                return True
            return False
    
    def _balance(self, parent, index):
        if index > 0 and len(parent.children[index - 1].keys) > self.order // 2:
            sibling = parent.children[index - 1]
            child = parent.children[index]
            child.keys.insert(0, parent.keys[index - 1])
            parent.keys[index - 1] = sibling.keys.pop()
            if not sibling.is_leaf:
                child.children.insert(0, sibling.children.pop())
        elif index < len(parent.children) - 1 and len(parent.children[index + 1].keys) > self.order // 2:
            sibling = parent.children[index + 1]
            child = parent.children[index]
            child.keys.append(parent.keys[index])
            parent.keys[index] = sibling.keys.pop(0)
            if not sibling.is_leaf:
                child.children.append(sibling.children.pop(0))
        else:
            if index > 0:
                index -= 1
            child = parent.children[index]
            sibling = parent.children[index + 1]
            child.keys.append(parent.keys.pop(index))
            child.keys.extend(sibling.keys)
            if not child.is_leaf:
                child.children.extend(sibling.children)
            parent.children.pop(index + 1)
    
    def print_tree(self):
        self._print_tree_recursive(self.root, 0)
    
    def _print_tree_recursive(self, node, level):
        print("Level", level, ":", node.keys)
        if not node.is_leaf:
            for child in node.children:
                self._print_tree_recursive(child, level + 1)


# Example usage
bplus_tree = BPlusTree(order=4)
keys_to_insert = [10, 20, 5, 30, 15, 25]

for key in keys_to_insert:
    bplus_tree.insert(key)

print("B+ Tree after insertion:")
bplus_tree.print_tree()

bplus_tree.delete(20)
print("\nB+ Tree after deleting key 20:")
bplus_tree.print_tree()

print("Search for key 15:", bplus_tree.search(15))  # Output: True
print("Search for key 25:", bplus_tree.search(25))  # Output: False
