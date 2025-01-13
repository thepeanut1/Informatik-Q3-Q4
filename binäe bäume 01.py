

class Binärbaum:
    def __init__(self):
        """create empty tree"""
        self.root = None

    def addItem(self, node, parent):
        if self.root == None:
            node = self.root
            
        elif node.value > parent.value and parent. right == None:
            parent.right = node
            print("New Node {node} was placed as the right child node of {parent}.")

        elif node.value < parent.value and parent.left == None:
            parent.left = node
            print("New Node {node} was placed as the left child node of {parent}.")

"""
Search for a certain Num.:
Try if num is bigger / smaller / same than root.
if Bigger go right
if smaller go left
repeat for following node till you find same
or you reach leaf (no children left/right), then you stop and conclude it aint in the tree


add Node to tree:
Node with a value is created
Node is sorted into tree with search method as a Child of a leaf
"""


class Node:
    def __init__(self, value):
        """create node without children"""
        self.value = value
        self.left = None
        self.right = None


tree01 = Binärbaum()
