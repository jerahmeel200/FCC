# Define a class for a tree node
class TreeNode:
    def __init__(self, key):
        self.key = key  # Store the key value of the node
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None

    def __str__(self):
        return str(self.key)  # Return the string representation of the key

# Define a class for the binary search tree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree as None

    # Helper method to recursively insert a key into the tree
    def _insert(self, node, key):
        if node is None:  # If the current node is None, create a new TreeNode
            return TreeNode(key)

        if key < node.key:  # If the key is smaller, go to the left subtree
            node.left = self._insert(node.left, key)
        elif key > node.key:  # If the key is larger, go to the right subtree
            node.right = self._insert(node.right, key)
        return node  # Return the updated node

    # Public method to insert a key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)  # Call the helper method starting from the root

    # Helper method to recursively search for a key in the tree
    def _search(self, node, key):
        if node is None or node.key == key:  # If the node is None or the key matches, return the node
            return node
        if key < node.key:  # If the key is smaller, search in the left subtree
            return self._search(node.left, key)
        return self._search(node.right, key)  # Otherwise, search in the right subtree

    # Public method to search for a key in the tree
    def search(self, key):
        return self._search(self.root, key)  # Call the helper method starting from the root

    # Helper method to recursively delete a key from the tree
    def _delete(self, node, key):
        if node is None:  # If the node is None, return None
            return node
        if key < node.key:  # If the key is smaller, go to the left subtree
            node.left = self._delete(node.left, key)
        elif key > node.key:  # If the key is larger, go to the right subtree
            node.right = self._delete(node.right, key)
        else:  # If the key matches the current node
            if node.left is None:  # If the left child is None, return the right child
                return node.right
            elif node.right is None:  # If the right child is None, return the left child
                return node.left

            # Replace the node's key with the smallest key in the right subtree
            node.key = self._min_value(node.right)
            # Delete the node with the smallest key in the right subtree
            node.right = self._delete(node.right, node.key)

        return node  # Return the updated node

    # Public method to delete a key from the tree
    def delete(self, key):
        self.root = self._delete(self.root, key)  # Call the helper method starting from the root

    # Helper method to find the minimum value in a subtree
    def _min_value(self, node):
        while node.left is not None:  # Traverse to the leftmost node
            node = node.left
        return node.key  # Return the key of the leftmost node

    # Helper method for inorder traversal of the tree
    def _inorder_traversal(self, node, result):
        if node:  # If the node is not None
            self._inorder_traversal(node.left, result)  # Traverse the left subtree
            result.append(node.key)  # Add the current node's key to the result
            self._inorder_traversal(node.right, result)  # Traverse the right subtree

    # Public method to perform inorder traversal of the tree
    def inorder_traversal(self):
        result = []  # Initialize an empty list to store the result
        self._inorder_traversal(self.root, result)  # Call the helper method starting from the root
        return result  # Return the result list

# Create an instance of the BinarySearchTree class
bst = BinarySearchTree()

# List of nodes to insert into the tree
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert each node into the binary search tree
for node in nodes:
    bst.insert(node)

# Search for the key 80 in the tree and print the result
print('Search for 80:', bst.search(80))

# Perform an inorder traversal of the tree and print the result
print("Inorder traversal:", bst.inorder_traversal())

# Delete the key 40 from the tree
bst.delete(40)

# Search for the key 40 in the tree after deletion and print the result
print("Search for 40:", bst.search(40))

# Perform an inorder traversal of the tree after deletion and print the result
print('Inorder traversal after deleting 40:', bst.inorder_traversal())
