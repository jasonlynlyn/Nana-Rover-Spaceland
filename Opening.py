import pygame
from pygame.locals import *
pygame.init()


Openingscreen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Nana Rover In Spaceland')

background = pygame.Surface(Openingscreen.get_size())
background = background.convert()
background.fill((250, 250, 250))

font = pygame.font.Font(None, 36)
text = font.render('Welcome to Nana Rover in Spaceland', 1, (10, 10, 10)) #draw text on new surface
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

Openingscreen.blit(background, (0, 0))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

	

