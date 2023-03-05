import pygame, time
from pygame.locals import *

bgColour = pygame.Color(60,90,170)

def main():

    pygame.init()
    playSurface = pygame.display.set_mode((1000,800))
    playSurface.fill(bgColour)
    pygame.display.set_caption('Lab7')
    time.sleep(5) 
    pygame.quit()
if __name__ == "__main__":
    main()