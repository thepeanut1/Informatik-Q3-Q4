class Header:
    def __init__(self):
        self.length = 0
        self.head = None
        self.end = None
        self.posInList = None

    def addItem(self, value):
        k = Node(value)
        self.length += 1
        
        if self.length == 1:
            self.head = k
            self.posInList = k
        else:
            self.end.nextNode = k

        self.end = k


    def printList(self):
        if self.length == 0:
            print("List is empty")
        else:
            while True:
                print(self.posInList.value)
                if self.posInList == self.end:
                    self.posInList = self.head
                    break
                self.posInList = self.posInList.nextNode

    def delKopf(self):
        if self.length > 0:
            value = self.head.value
            self.head = self.head.nextNode
            self.length -= 1
            if self.length == 0:
                self.end = None
            return value

        else:
            print("Die Liste ist leer")


    def delItem(self, item):
        self.end = self.head
        if self.length == 0:
            print("List is empty")
        else:
            itemDeleted = False
            while True:
                if self.end.value == item:
                    itemDeleted = True
                    if self.end == self.head:
                        self.delKopf()
                    elif self.end.nextNode == None:
                        self.end = prevNode
                        print(f"deleting {item}2")
                        prevNode.nextNode = None
                        break
                    else:
                        print(f"deleting {item}")
                        prevNode.nextNode = self.end.nextNode
                    
                    
                    
                    
                if self.end.nextNode == None:
                    break
                prevNode = self.end
                self.end = self.end.nextNode

            if itemDeleted == False:
                print(f"{item} was not found.")


class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


list1 = Header()
list1.addItem(1)
list1.addItem(3)
list1.addItem(True)
list1.addItem(78)

list1.addItem(2)
list1.addItem("test")

list1.printList()
print("\n")
list1.delItem(1)

list1.printList()

#list1.printList()
    
