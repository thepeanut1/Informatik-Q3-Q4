import random

colors = ["Yellow", "Green", "Blue", "Red"]
numbers = [1,2,4,5,6,7,8,9]

class Cards:
    def __init__(self, cardID, color, number):
        self.cardID = cardID
        self.color = color
        self.number = number

stack = []

for color in colors:
    for num in numbers:
        card = Cards((color,num), color, num)
        stack.append(card)


random.shuffle(stack)
print(stack[0].cardID)
print("\n")
for i in range(5):
    print(stack[i].cardID)

class Player:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.deck = []


    def check_cards(self):
        pass

    def hide_cards(self):
        pass
    def show_cards(self):
        pass

    def give_cards(self):
        for i in range(5):
            self.deck.append(stack[i])
        for i in range(5):
            stack.pop(i)


p1 = Player(1, "Bean")
p1.give_cards()

p2 = Player(2, "Peanut")
p2.give_cards()

print("\n")
for i in range(5):
    print(stack[i].cardID)
print("\n")
for i in range(5):
    print(p1.deck[i].cardID)
