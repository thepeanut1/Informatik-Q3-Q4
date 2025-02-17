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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.blit(bg,[0,0])

    for i in range(len(myCard)):
        spacing = 400 / len(myCard)
        screen.blit(pygame.transform.scale(pygame.image.load("cards/"+myCard[i].color+"_"+str(myCard[i].number)+".jpg"),[150,150]),[spacing * i + 400, 700])


    if len(gameManager.playerlist) == 2:
        for i in range(len(gameManager.playerlist[1].deck)):
            spacing = 300 / len(gameManager.playerlist[1].deck)
            screen.blit(pygame.transform.scale(pygame.image.load("cards/back.png"),[150,150]),[spacing * i + 425, 100])
        
    if len(gameManager.playerlist) == 3:
        for i in range(len(gameManager.playerlist[playerID + 2].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 2].deck)
            screen.blit(pygame.transform.scale(pygame.image.load("cards/back.png"),[150,150]),[spacing * i + 425, 100])
 
        for i in range(len(gameManager.playerlist[playerID + 1].deck)):
            spacing = 300 / len(gameManager.playerlist[playerID + 1].deck)
            screen.blit(pygame.transform.scale(pygame.image.load("cards/back.png"),[150,150]),[100, spacing * i + 200])

    pygame.display.flip()

    
    dt = clock.tick(60) / 1000













#py -m pip install -U pygame --user

#https://www.pygame.org/docs/
#https://www.unorules.com/
#https://png.pngtree.com/thumb_back/fw800/background/20221002/pngtree-green-poker-table-view-felt-pattern-photo-image_615707.jpg
#https://gamedevacademy.org/pygame-background-image-tutorial-complete-guide/
