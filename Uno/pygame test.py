import pygame
import gameManager

pygame.init()
screen = pygame.display.set_mode((1280,900))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0

bg = pygame.image.load("bg.png")

playerID = 0
myCard = gameManager.playerlist[playerID].deck


def cardSelected(i):
    selected_card = myCard[i]
    #to do: send selected card to server
    #to do: receive move validity from server
    if validMove:
        myCard.pop(i)
        validMove = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mcords = pygame.mouse.get_pos()
            print(mcords)
            if mcords[0] > 400 and mcords[0] < 905 and mcords[1] > 700 and mcords [1] < 550:
                
                for i in range(len(myCard)):
                    if mcords[0] < 400 + (i+1) * spacing:
                        cardSelected(i)



    screen.blit(bg,[0,0])

    for i in range(len(myCard)):
        spacing = 400 / len(myCard)
        screen.blit(pygame.transform.scale(pygame.image.load("cards/"+myCard[i].color+"_"+str(myCard[i].number)+".jpg"),[105,150]),[spacing * i + 400, 700])


    if len(gameManager.playerlist) == 2:
        for i in range(len(gameManager.playerlist[1].deck)):
            spacing = 300 / len(gameManager.playerlist[1].deck)
            
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), 180),[spacing * i + 425, 100])
        
    if len(gameManager.playerlist) == 3:
        for i in range(len(gameManager.playerlist[playerID + 2].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 2].deck)
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), 180),[spacing * i + 425, 100])
 
        for i in range(len(gameManager.playerlist[playerID + 1].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 1].deck)
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), -90),[100, 500 - spacing * i])

    if len(gameManager.playerlist) == 4:
        for i in range(len(gameManager.playerlist[playerID + 2].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 2].deck)
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), 180),[spacing * i + 425, 100])
 
        for i in range(len(gameManager.playerlist[playerID + 1].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 1].deck)
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), -90),[100, 500 - spacing * i])

        for i in range(len(gameManager.playerlist[playerID + 3].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 3].deck)
            screen.blit(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards/back.png"),[97,150]), 90),[1000, 500 - spacing * i])


    pygame.display.flip()

    
    dt = clock.tick(60) / 1000













#py -m pip install -U pygame --user

#https://www.pygame.org/docs/
#https://www.unorules.com/
#https://png.pngtree.com/thumb_back/fw800/background/20221002/pngtree-green-poker-table-view-felt-pattern-photo-image_615707.jpg
#https://gamedevacademy.org/pygame-background-image-tutorial-complete-guide/
