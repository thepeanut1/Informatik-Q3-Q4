import random

colors = ["Yellow", "Green", "Blue", "Red"]
numbers = [1,2,3,4,5,6,7,8,9,"Draw_2", "Skip", "Reverse"]
wilds = ["Wish", "Draw_4"]


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
            for i in range(7):
                
                self.deck.append(stack[i])
            for i in range(7):
                stack.pop(i)

class Cards:
        def __init__(self, cardID, color, number, function):
            self.cardID = cardID
            self.color = color
            self.number = number
            self.function = function

def play_card(selected_card):
        if selected_card.color == playedcards[-1].color or selected_card.number == playedcards[-1].number:
                playedcards.append(selected_card)
                player.deck.pop(selected_card)
        elif selected_card.color == "Wild":
                playedcards.append(selected_card)
                #execute function
                player.deck.pop(selected_card)


def turn(p):
    p.show_cards()
    print("selected_card")
    

def start_game():
    global stack
    stack = []

    #for i in range(2):
            #for 
    for i in range(2):
            for color in colors:
                for num in numbers:
                    card = Cards((color,num), color, num, None)
                    stack.append(card)


    random.shuffle(stack)
    #print(stack[0].cardID)
    print("\n")
    print(len(stack))
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
    for i in range(7):
        print(playerlist[0].deck[i].cardID)
    print("\n")
    for i in range(7):
        print(playerlist[1].deck[i].cardID)

    print("\n")
    print(len(stack))
    for i in range(5):
        print(stack[i].cardID)

    turn(playerlist[0])


start_game()
