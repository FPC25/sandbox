#Binary Tree Search algorithm

class BSTNode:
    def __init__(self, val=None):
        """
        Initialize a Binary Search Tree (BST) node.
        Each node has a value, and pointers to left and right child nodes.
        """
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node
        self.val = val  # Value of the node

    def insert(self, val):
        """
        Insert a value into the BST. Duplicates are not allowed.
        """
        if not self.val:  # If the current node is empty, set its value
            self.val = val
            return

        if self.val == val:  # If the value already exists, do nothing
            return

        if val < self.val:  # If the value is less, go to the left subtree
            if self.left:
                self.left.insert(val)  # Recursively insert into the left subtree
                return
            self.left = BSTNode(val)  # Create a new node if left child is empty
            return

        # If the value is greater, go to the right subtree
        if self.right:
            self.right.insert(val)  # Recursively insert into the right subtree
            return
        self.right = BSTNode(val)  # Create a new node if right child is empty
        return

    def get_min(self):
        """
        Find the minimum value in the BST.
        Traverse the left subtree until the leftmost node is reached.
        """
        current = self
        while current.left is not None:  # Keep going left until no more left child
            current = current.left
        return current.val

    def get_max(self):
        """
        Find the maximum value in the BST.
        Traverse the right subtree until the rightmost node is reached.
        """
        current = self
        while current.right is not None:  # Keep going right until no more right child
            current = current.right
        return current.val

    def delete(self, val):
        """
        Delete a value from the BST.
        Handles three cases:
        1. Node to be deleted has no children.
        2. Node to be deleted has one child.
        3. Node to be deleted has two children.
        """
        if not self.val:  # If the tree or node is empty, return None
            return None

        if val < self.val:  # If the value is less, go to the left subtree
            if self.left:
                self.left = self.left.delete(val)  # Recursively delete from the left subtree
            return self

        if val > self.val:  # If the value is greater, go to the right subtree
            if self.right:
                self.right = self.right.delete(val)  # Recursively delete from the right subtree
            return self

        # If the node to be deleted has no right child, return the left child
        if not self.right:
            return self.left

        # If the node to be deleted has no left child, return the right child
        if not self.left:
            return self.right

        # If the node has two children, replace its value with the smallest value
        # in the right subtree and delete that smallest value
        new = self.right.get_min()
        self.val = new  # Update the current node's value
        self.right = self.right.delete(new)  # Delete the duplicate value
        return self

    def preorder(self, visited):
        """
        Perform a preorder traversal (root -> left -> right).
        Append the values to the visited list.
        """
        visited.append(self.val)  # Visit the root
        if self.left is not None:  # Traverse the left subtree
            visited = self.left.preorder(visited)
        if self.right is not None:  # Traverse the right subtree
            visited = self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        """
        Perform a postorder traversal (left -> right -> root).
        Append the values to the visited list.
        """
        if self.left is not None:  # Traverse the left subtree
            visited = self.left.postorder(visited)
        if self.right is not None:  # Traverse the right subtree
            visited = self.right.postorder(visited)
        visited.append(self.val)  # Visit the root
        return visited

    def inorder(self, visited):
        """
        Perform an inorder traversal (left -> root -> right).
        Append the values to the visited list.
        """
        if self.left is not None:  # Traverse the left subtree
            visited = self.left.inorder(visited)
        visited.append(self.val)  # Visit the root
        if self.right is not None:  # Traverse the right subtree
            visited = self.right.inorder(visited)
        return visited

    def exists(self, val):
        """
        Check if a value exists in the BST.
        Returns True if the value exists, otherwise False.
        """
        if val < self.val:  # If the value is less, search in the left subtree
            if self.left is not None:
                return self.left.exists(val)
            return False

        if val > self.val:  # If the value is greater, search in the right subtree
            if self.right is not None:
                return self.right.exists(val)
            return False

        return True  # If the value matches the current node's value
    
    def height(self):
        """
        Calculate the height of the BST.
        The height of a tree is the number of edges on the longest path 
        from the root node to a leaf node. An empty tree has a height of 0.

        Returns:
            int: The height of the tree.
        """
        if self.val is None:  # If the node is empty, return height as 0
            return 0

        # Calculate the height of the left subtree
        left_height = 0
        if self.left is not None:
            left_height = self.left.height()

        # Calculate the height of the right subtree
        right_height = 0
        if self.right is not None: 
            right_height = self.right.height()
            
        # Return the maximum height between left and right subtrees, plus 1 for the current node
        return max(left_height, right_height) + 1