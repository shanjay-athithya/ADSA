class BPlusTreeNode:
    def __init__(self, is_leaf=True):
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

class BPlusTree:
    def __init__(self, degree):
        self.root = BPlusTreeNode()
        self.degree = degree

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.degree - 1:
            new_root = BPlusTreeNode(is_leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.is_leaf:
            index = len(node.keys) - 1
            while index >= 0 and key < node.keys[index]:
                index -= 1
            node.keys.insert(index + 1, key)
        else:
            index = len(node.keys) - 1
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == 2 * self.degree - 1:
                self._split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key)

    def _split_child(self, parent, index):
        degree = self.degree
        child = parent.children[index]
        new_child = BPlusTreeNode(is_leaf=child.is_leaf)
        
        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)
        
        new_child.keys = child.keys[degree:]
        child.keys = child.keys[:degree - 1]
        
        if not child.is_leaf:
            new_child.children = child.children[degree:]
            child.children = child.children[:degree]

    def delete(self, key):
        self._delete_key(self.root, key)
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]

    def _delete_key(self, node, key):
        if node.is_leaf:
            if key in node.keys:
                node.keys.remove(key)
        else:
            index = 0
            while index < len(node.keys) and key > node.keys[index]:
                index += 1

            if index < len(node.keys) and key == node.keys[index]:
                if len(node.children[index].keys) >= self.degree:
                    predecessor = self._get_predecessor(node, index)
                    node.keys[index] = predecessor.keys[-1]
                    self._delete_key(node.children[index], predecessor.keys[-1])
                elif len(node.children[index + 1].keys) >= self.degree:
                    successor = self._get_successor(node, index)
                    node.keys[index] = successor.keys[0]
                    self._delete_key(node.children[index + 1], successor.keys[0])
                else:
                    self._merge_children(node, index)
                    self._delete_key(node.children[index], key)
            else:
                if len(node.children[index].keys) < self.degree:
                    self._fill_child(node, index)
                self._delete_key(node.children[index], key)

    def _get_predecessor(self, node, index):
        current = node.children[index]
        while not current.is_leaf:
            current = current.children[-1]
        return current

    def _get_successor(self, node, index):
        current = node.children[index + 1]
        while not current.is_leaf:
            current = current.children[0]
        return current

    def _merge_children(self, parent, index):
        child = parent.children[index]
        sibling = parent.children[index + 1]
        
        child.keys.append(parent.keys.pop(index))
        child.keys.extend(sibling.keys)
        if not child.is_leaf:
            child.children.extend(sibling.children)
        
        parent.children.pop(index + 1)

    def _fill_child(self, parent, index):
        if index > 0 and len(parent.children[index - 1].keys) >= self.degree:
            self._borrow_from_prev(parent, index)
        elif index < len(parent.children) - 1 and len(parent.children[index + 1].keys) >= self.degree:
            self._borrow_from_next(parent, index)
        elif index < len(parent.children) - 1:
            self._merge_children(parent, index)
        else:
            self._merge_children(parent, index - 1)

    def _borrow_from_prev(self, parent, index):
        child = parent.children[index]
        sibling = parent.children[index - 1]
        
        child.keys.insert(0, parent.keys[index - 1])
        parent.keys[index - 1] = sibling.keys.pop()
        if not sibling.is_leaf:
            child.children.insert(0, sibling.children.pop())

    def _borrow_from_next(self, parent, index):
        child = parent.children[index]
        sibling = parent.children[index + 1]
        
        child.keys.append(parent.keys[index])
        parent.keys[index] = sibling.keys.pop(0)
        if not sibling.is_leaf:
            child.children.append(sibling.children.pop(0))

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level):
        if node:
            print("Level", level, ":", node.keys)
            if not node.is_leaf:
                for child in node.children:
                    self._print_tree_recursive(child, level + 1)


if __name__ == "__main__":
    b_plus_tree = BPlusTree(degree=2)
    keys = [3, 7, 12, 14, 15, 16]
    for key in keys:
        b_plus_tree.insert(key)

    print("B+ Tree after insertion:")
    b_plus_tree.print_tree()

    b_plus_tree.delete(16)

    print("\nB+ Tree after deleting key 16:")
    b_plus_tree.print_tree()
