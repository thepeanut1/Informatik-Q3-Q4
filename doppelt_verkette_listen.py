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
