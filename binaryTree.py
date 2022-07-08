class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None    # Left Child
        self.right = None   # Right Child
        self.data = data    # Node Data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def valExists(self, target):
        
        if target < self.data:
            if self.left: 
                return self.left.valExists(target) # recursively check the left tree
            else:
                return False        # can't go any further- so return false
        elif target > self.data:
            if self.right:
                return self.right.valExists(target)
            else:
                return False
        else:
            return True

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()