import random, pygame, sys, time
from pygame.locals import *

FPS = 10
pygame.init()
pygame.display.init()
pygame.mixer.init()
pygame.font.init()

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

def OpeningDescription():
    screen_width = 1200
    screen_height = 1000
    screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
    pygame.display.set_caption("Hero's Journey")
    FPSCLOCK = pygame.time.Clock()
    screen.fill(black)
    pygame.display.update()
    while True:
        font = pygame.font.SysFont("Arial", 20,bold=True,italic=False)
        font1 = pygame.font.SysFont("Arial",40,bold=True,italic=False)
        font2 = pygame.font.SysFont("Arial",25,bold=True,italic=False)
        font3 = pygame.font.SysFont("Arial",25,bold=True,italic=True)

        text0 = "Hero's Journey"
        text = "Our hero is looking to pass through a hidden door way to retrieve an old object of great value and power."
        text1 = "She has found a sort of Rosetta stone at the side of a mountain which has the following message inscribed on it in three languages."
        text2 = "English:  Sing!     Unknown Language: hoyalat:as!     Latin: canta!"
        text3 = "She knows English and Latin and decided -- what the heck -- I'll sing."
        text4 = "Upon singing, a doorway appeared in the side of the mountain along with an inscription on the doorway."
        text5 = "The inscription is:  addakhas dorvofaan davvey azhas cheyaosaan akat dak "
        text6 = "The inscription is in a language unknown to our hero, but it looks like it might be the same as the unknown language on the Rosetta type stone."
        text7 = "This means that there might be some other clues to this unknown language in the enviroment."
        text8 = "Our hero goes out to gather these clues."
        text9 = "Press Enter key to start the journey!"

        displaytext0 = font1.render(text0,True,white)
        screen.blit(displaytext0,(100,0))
        displaytext = font.render(text,True,white)
        screen.blit(displaytext,(100,100))
        displaytext1 = font.render(text1,True,white)
        screen.blit(displaytext1,(100,125))
        displaytext2 = font3.render(text2,True,white)
        screen.blit(displaytext2,(100,175))
        displaytext3 = font.render(text3,True,white)
        screen.blit(displaytext3,(100,225))
        displaytext4 = font.render(text4,True,white)
        screen.blit(displaytext4,(100,250))
        displaytext5 = font3.render(text5,True,white)
        screen.blit(displaytext5,(100,300))
        displaytext6 = font.render(text6,True,white)
        screen.blit(displaytext6,(100,350))
        displaytext7 = font.render(text7,True,white)
        screen.blit(displaytext7,(100,375))
        displaytext8 = font.render(text8,True,white)
        screen.blit(displaytext8,(100,425))
        displaytext9 = font2.render(text9,True,yellow)
        screen.blit(displaytext9,(100,500))

        response = None
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    response = 'NEXT'
        if response == 'NEXT':
            break
			
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    pygame.quit()
	
OpeningDescription()