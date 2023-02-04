from un import *
import pygame
import math
class Player:
	def __init__(self):
		self.x,self.y = player_pos
		self.angle = player_angle
        
	@property
	def pos(self):
		return(self.x,self.y)

	def movement(self):
		rel_x, rel_y = pygame.mouse.get_pos()
		self.angle = (rel_y/2*0.02)
		self.angle = (rel_x/2*0.02)
		keys = pygame.key.get_pressed()
		event = pygame.event.get()
		sin_a=math.sin(self.angle)
		cos_a=math.cos(self.angle)
		if keys[pygame.K_w]:
			self.x += player_speed*cos_a
			self.y += player_speed*sin_a
		if keys[pygame.K_s]:
			self.x += -player_speed*cos_a
			self.y += -player_speed*sin_a
		if keys[pygame.K_a]:
			self.x += player_speed*sin_a
			self.y += -player_speed*cos_a
		if keys[pygame.K_d]:
			self.x += -player_speed*sin_a
			self.y += player_speed*cos_a
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02

		
		
		