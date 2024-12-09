class Header:
    def __init__(self):
        self.length = 0
        self.head = None
        self.end = None
        self.posInList = None

    def addItem(self, value):
        k = Node(value)                 #1. Erzeugen einer Instanz der Klasse Knoten,
        #self.length += 1               #   die die Daten beinhalten, die wir einfügen möchten
        
        if self.length == 0:        #(1)   2.a Wenn die Liste leer, dann wird k self.kopf zugewiesen
            self.head = k           
            self.posInList = k
        else:                       #2.b sonst zeigt der Zeiger nächster des bisherigen letzten Knoten auf k
            self.end.nextNode = k
        self.length += 1            #3. k wird als Ende der Liste festgelegt
        self.end = k                #4. Länge der Liste wird (um 1) inkrementiert


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

    def del_and_show(self):
        if self.length > 0:
            value = self.head.value
            self.head = self.head.nextNode
            self.length -= 1
            if self.length == 0:
                self.end = None
            return value

        else:
            print("Die Liste ist leer")


    def delitem(self, item):
        self.end = self.head
        if self.length == 0:
            print("List is empty")
        else:
            itemdeleted = False
            while True:
                #print(self.posInList.value)
                if self.end.value == item:
                    itemdeleted = True
                    if self.end.value == self.head:
                        self.del_and_show()
                    elif self.end.nextNode == None:
                        self.end = prevNode
                        print(f"deleted item: {item}")
                        prevNode.nextNode = None
                        #self.end = self.head
                        break

                    else:
                        print(f"deleted item: {item}")
                        prevNode.nextNode = self.end.nextNode
                    
                if self.end.nextNode == None:
                    break
                prevNode = self.end
                self.end = self.end.nextNode
                
            if itemdeleted == False:
                print(f"item: {item} not found")



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



"""
list1.delKopf()
list1.delKopf()
list1.delKopf()
list1.delKopf()
list1.delKopf()
"""


list1.printList()
#list1.printList()
print("\n")
list1.delitem("test")
list1.printList()


#list1.printList()
    


"""
    def delKopf(self):
        self.length -= 1
        if self.head == self.end:
            self.head = None
        else:
            self.head = self.head.nextNode

        self.posInList = self.head
"""
