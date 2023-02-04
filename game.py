import pygame
from un import *
from player import Player
import math 
from bu import world_map
from ray import ray_casting
from drawing import Drawing
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc,sc_map)

while True:
	print(pygame.mouse.get_pos())
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	player.movement()
	sc.fill(BLACK)
	drawing.background()
	drawing.world(player.pos,player.angle)
	drawing.fps(clock)

	

	pygame.display.flip()
	clock.tick()
