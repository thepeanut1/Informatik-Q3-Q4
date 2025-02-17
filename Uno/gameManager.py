import random

colors = ["Yellow", "Green", "Blue", "Red"]
numbers = [1,2,4,5,6,7,8,9]


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

class Cards:
        def __init__(self, cardID, color, number):
            self.cardID = cardID
            self.color = color
            self.number = number


def turn(p):
    p.show_cards()

def start_game():
    global stack
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
    global playerlist
    playerlist = []


    for i in range(playeramount):
        player = Player(i, input(f"Player {i}, please enter a name:"))
        playerlist.append(player)
        player.give_cards()
        print(i)


    playedcards = []
    playedcards.append(stack[0])
    stack.pop(1)

    print("\n")
    for i in range(5):
        print(playerlist[0].deck[i].cardID)
    print("\n")
    for i in range(5):
        print(playerlist[1].deck[i].cardID)

    print("\n")
    for i in range(5):
        print(stack[i].cardID)

    turn(playerlist[0])


start_game()
