class Header:
    def __init__(self):
        self.length = 0
        #self.head = None
        self.end = None
        self.posInList = None

    def addItem(self, value):
        k = Node(value)         

        if self.length == 0:       
            k.nextNode = k
            self.posInList = k

        else:                       
            k.prevNode = self.end
            k.nextNode = self.end.nextNode
            self.end.nextNode = k
            

        self.length += 1
        self.end = k             


    def printList(self):
        if self.length == 0:
            print("List is empty")
        else:
            while True:
                print(self.posInList.value)
                if self.posInList == self.end:
                    self.posInList = self.end.nextNode
                    break
                self.posInList = self.posInList.nextNode



    def isEmpty(self):
        self.length = -10
        if self.length == 0:
            print("List is empty")

        elif self.length <0:
            print('''
█░█ █▀█ █░█░█  █▀▄ █ █▀▄  █▄█ █▀█ █░█  █▀▄ █▀█  ▀█▀ █░█ █ █▀ ▀█
█▀█ █▄█ ▀▄▀▄▀  █▄▀ █ █▄▀  ░█░ █▄█ █▄█  █▄▀ █▄█  ░█░ █▀█ █ ▄█ ░▄
                  ''')
            

        else:
            print("List is not empty")
            
    def delete(self, item):
        if self.length == 0:
            print("List is empty")
        else:
            while True:
                if self.posInList.value == item:
                    print(f"deleting {item}")
                    if self.posInList == self.end.nextNode:
                        self.posInList.nextNode.prevNode = None
                        self.end.nextNode = self.posInList.nextNode
                    elif self.posInList == self.end:
                        self.end = self.posInList.prevNode
                        self.posInList.prevNode.nextNode = self.posInList.nextNode
                    else:
                        self.posInList.nextNode.prevNode = self.posInList.prevNode
                        self.posInList.prevNode.nextNode = self.posInList.nextNode
                if self.posInList == self.end:                    
                    self.posInList = self.end.nextNode
                    break
                self.posInList = self.posInList.nextNode
    
    def insertItem(self, pos_von, item):
        k = Node(item)
        while True:

                if self.end.nextNode.value == pos_von:
                    #print("wiener")
                    self.end.nextNode.prevNode = k
                    k.nextNode = self.end.nextNode
                    self.end.nextNode = k


                if self.posInList.value == pos_von:
                    self.posInList.prevNode.nextNode = k
                    self.posInList.prevNode = k
                    k.nextNode = self.posInList
                    k.prevNode = self.posInList.prevNode
                    print("yea")
                    
                if self.posInList == self.end:
                    print("test1")
                    self.posInList = self.end.nextNode
                    self.length += 1
                    break

                self.posInList = self.posInList.nextNode


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None




list1 = Header()
list1.addItem(1)
list1.addItem(3)
list1.addItem(True)
list1.addItem(78)
list1.addItem(2)
list1.addItem("test")

list1.printList()
list1.isEmpty()
