import random
from player import *

colors = ["Yellow", "Green", "Blue", "Red"]
numbers = [1,2,4,5,6,7,8,9]


def start_game():
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
    #print(stack[0].cardID)
    print("\n")
    for i in range(5):
        print(stack[i].cardID)

    playeramount = int(input("Please enter the number of players:"))
    playerlist = []


    for i in range(playeramount):
        player = Player(i+1, input(f"Player {i+1}, please enter a name:"))
        playerlist.append(player)
        player.give_cards()


    print("\n")
    for i in range(5):
        print(playerlist[0].deck[i].cardID)
    print("\n")
    for i in range(5):
        print(playerlist[1].deck[i].cardID)

    


start_game()
