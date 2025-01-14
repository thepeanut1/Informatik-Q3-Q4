from Turtle import *

class Binärbaum:
    def __init__(self):
        """create empty tree"""
        self.root = None
        self.current_counter = -1
        self.height = 0

    def addItem(self, val, node = None, parent = None):
        self.current_counter +=1
        if parent == None:
            print("Root was assigned to parent")
            parent = self.root

            print("Node was created")
            node = Node(val)

        if self.root == None:
            print("Root was created\n")
            self.root = node
            return 

        elif node.value > parent.value and parent.right == None:
            parent.right = node
            print(f"New Node {node.value} was placed as the right child node of {parent.value}.")

        elif node.value <= parent.value and parent.left == None:
            parent.left = node
            print(f"New Node {node.value} was placed as the left child node of {parent.value}.")

        elif node.value > parent.value:
            print(f"Function was called again.\nOld parent: {parent.value}\nNew parent: {parent.right.value}")
            return self.addItem(val, node, parent.right)
        
        elif node.value <= parent.value:
            print(f"Function was called again.\nOld parent: {parent.value}\nNew parent: {parent.left.value}")
            return self.addItem(val, node, parent.left)
        
        print(f"{val} added \n \n")
        if self.current_counter > self.height:
            self.height = self.current_counter

        self.current_counter = 0

    def listToTree(self, l, posInList = 0):
        if posInList == len(l):
            print("List is now in Tree")
            return
        else:
            self.addItem(l[posInList])
            posInList += 1
            return self.listToTree(l, posInList)

    def findItem(self, val, currNode = None):
        if currNode == None:
            currNode = self.root
        print(currNode.value)
        if val == currNode.value:
            print("Value was found")

        elif val > currNode.value:
            if currNode.right == None:
                print(f"{val} not found")
            else:
                print("Function was called again")
                return self.findItem(val,currNode.right)
        
        elif val < currNode.value:
            if currNode.left == None:
                print(f"{val} not found")
            else:
                print("Function was called again")
                return self.findItem(val,currNode.left)
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

"""
tree01.addItem(5)
tree01.addItem(34)
tree01.addItem(4)
tree01.addItem(8)
tree01.addItem(324)
tree01.addItem(33)
tree01.addItem(23)
"""
list1 = [3,5,2,5,8,3,5,2,6,8,3,4,6,3,4,]

tree01.listToTree(list1)

tree01.findItem(6)
