class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    
    def _insert_recursive(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        elif new_node.value > current_node.value:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)
    
    def in_order_traversal(self, node, result=[]):
        if node is None:
            return
        self.in_order_traversal(node.left, result)
        result.append(node.value)
        self.in_order_traversal(node.right, result)
        return result

def build_tree(elements):
    tree = BinarySearchTree()
    for element in elements:
        tree.insert(element)
    
    return tree
    
def print_tree_structure(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree_structure(node.left, level + 1, "L--- ")
            print_tree_structure(node.right, level + 1, "R--- ")



elements = [45, 27, 67, 36, 56, 15, 75, 31, 53, 39, 64]
bst_tree = build_tree(elements)

print_tree_structure(bst_tree.root)

# Perform in-order traversal and print the values
in_order_result = bst_tree.in_order_traversal(bst_tree.root)
print("In-order traversal result:", in_order_result)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    
    def _insert_recursive(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        elif new_node.value > current_node.value:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)
    
    def postorder_traversal(self, node, result=None):
        if result is None:
            result = []
        if node is not None:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

    def left_rotation(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
    def right_rotation(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root
    
    def left_right_rotation(self, node):
        node.left = self.left_rotation(node.left)
        return self.right_rotation(node)
    
    def right_left_rotation(self, node):
        node.right = self.right_rotation(node.right)
        return self.left_rotation(node)

    def balance_tree(self, node):
        if node is None:
            return node
        
        # Calculate balance factor
        balance_factor = self.get_balance_factor(node)
        
        # Left heavy
        if balance_factor > 1:
            # Left-Left case
            if self.get_balance_factor(node.left) >= 0:
                return self.right_rotation(node)
            # Left-Right case
            else:
                return self.left_right_rotation(node)
        
        # Right heavy
        if balance_factor < -1:
            if self.get_balance_factor(node.right) <= 0:
                return self.left_rotation(node)
            else:
                return self.right_left_rotation(node)
        
        return node

    def get_balance_factor(self, node):
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return left_height - right_height
    
    def get_height(self, node):
        if node is None:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

elements = [45, 27, 67, 36, 56, 15, 75, 31, 53, 39, 64]

# Build the binary search tree
bst_tree = BinarySearchTree()
for element in elements:
    bst_tree.insert(element)

# Print the content of the tree before balancing
print("Tree content before balancing (Postorder Traversal):", bst_tree.postorder_traversal(bst_tree.root))

# Adding unbalanced elements
unbalanced_elements = [10, 5, 20]
for element in unbalanced_elements:
    bst_tree.insert(element)

# Printing the content of the tree after adding unbalanced elements
print("Tree content after adding unbalanced elements (Postorder Traversal):", bst_tree.postorder_traversal(bst_tree.root))

# Rebalancing the tree
bst_tree.root = bst_tree.balance_tree(bst_tree.root)

# Printing the content of the tree after balancing
print("Tree content after balancing (Postorder Traversal):", bst_tree.postorder_traversal(bst_tree.root))
