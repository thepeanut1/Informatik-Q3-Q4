from turtle import Turtle
from random import randint


class Binärbaum:
    def __init__(self):
        """create empty tree"""
        self.root = None
        self.current_counter = -1
        self.height = 0

    def addItem(self, val, node = None, parent = None):
        self.current_counter +=1
        if parent == None:
            parent = self.root

            node = Node(val)

        if self.root == None:
            self.root = node
            return 

        elif node.value > parent.value and parent.right == None:
            parent.right = node

        elif node.value <= parent.value and parent.left == None:
            parent.left = node

        elif node.value > parent.value:
            return self.addItem(val, node, parent.right)
        
        elif node.value <= parent.value:
            return self.addItem(val, node, parent.left)
        
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
        if val == currNode.value:
            print("Value was found")

        elif val > currNode.value:
            if currNode.right == None:
                print(f"{val} not found")
            else:
                return self.findItem(val,currNode.right)
        
        elif val < currNode.value:
            if currNode.left == None:
                print(f"{val} not found")
            else:
                return self.findItem(val,currNode.left)
            
    def drawTree(self):
        if self.height > 7:
            print("Tree height over 7\nto many levels to print")
            return
        t = Turtle()
        t.speed(0)
        t.hideturtle()
        t.screen.screensize(800,800)
        t.penup()
        t.pencolor("red")
        t.goto(0,380)
        t.write(self.root.value, align="center")

        if self.root.right != None:
            t.pendown()
            t.goto((t.xcor() + 400/2**1), (t.ycor()-100))
            self.drawRight(self.root.right,2, t.pos())

        if self.root.left != None:
            t.pendown()
            t.goto(0,380)
            t.goto((t.xcor() - 400/2**1), (t.ycor()-100))
            self.drawLeft(self.root.left,2, t.pos())

    def drawRight(self, node, depth, prevPos):
        right = Turtle()
        right.speed(0)
        right.hideturtle()
        right.penup()
        right.pencolor("green")
        right.goto(prevPos)
        right.write(node.value, align="left")

        if node.right != None:
            right.pendown()
            right.goto((right.xcor() + 400/(2**depth)), (right.ycor()-100))
            self.drawRight(node.right, depth +1, right.pos())

        if node.left != None:
            right.penup()
            right.goto(prevPos)
            right.pendown()
            right.goto((right.xcor() - 400/(2**depth)), (right.ycor()-100))
            self.drawLeft(node.left, depth +1, right.pos())
        
    def drawLeft(self, node, depth, prevPos):
        left = Turtle()
        left.speed(0)
        left.hideturtle()
        left.penup()
        left.pencolor("blue")
        left.goto(prevPos)
        left.write(node.value, align="right")

        if node.right != None:
            left.pendown()
            left.goto((left.xcor() + 400/(2**depth)), (left.ycor()-100))
            self.drawRight(node.right, depth +1, left.pos())

        if node.left != None:
            left.penup()
            left.goto(prevPos)
            left.pendown()
            left.goto((left.xcor() - 400/(2**depth)), (left.ycor()-100))
            self.drawLeft(node.left, depth +1, left.pos())

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
list1 = [100,50,25,10,5,11,28,26,45,75,70,83,86,76,72,60,150,143,146,149,129,140,111,145,160,154,156,151,170,169,175]

def makeList(length):
    l = [500]
    for i in range(length-1):
        l.append(randint(100,999))
    print(l)
    return l

tree01.listToTree(list1)

tree01.findItem(6)

tree01.drawTree()

t = input("Press enter to close window:")
