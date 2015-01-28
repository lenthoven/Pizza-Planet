import pygame
import random
pygame.init()
screen = pygame.display.set_mode((480,360))

up = False
down = False
right = False
left = False
class Player:
	def __init__(self):
		self.playerList = [pygame.image.load("images/cave.png"), pygame.image.load("images/character.png").convert_alpha(), pygame.image.load("images/character2.png").convert_alpha(),pygame.image.load("images/character3.png").convert_alpha(),pygame.image.load("images/character4.png").convert_alpha()]
		self.playerx = 0
		self.playery = 0
		self.characterx = 220
		self.charactery = 150
		self.move = 0
		self.costume = 1
	def checkOff(self):
		if self.playerx >= 0:
			self.playerx = 0
		if self.playerx <= -1920:
			self.playerx = -1920
		if self.playery >= 0:
			self.playery = 0
		if self.playery <= -1440:
			self.playery = -1440
	def draw(self,aScreen):
		aScreen.blit(self.playerList[0],(self.playerx,self.playery))
		aScreen.blit(self.playerList[self.costume],(self.characterx,self.charactery))
	def left(self):
		self.playerx += .1
		self.costume = 1
	def right(self):
		self.playerx -= .1
		self.costume = 2
	def up(self):
		self.playery += .1
		self.costume = 3
	def down(self):
		self.playery -= .1
		self.costume = 4
		
Player = Player()
screen = pygame.display.set_mode((480,360))
running = True
while running:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				left = True
			if event.key == pygame.K_RIGHT:
				right = True
			if event.key == pygame.K_UP:
				up = True
			if event.key == pygame.K_DOWN:
				down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				left = False
			if event.key == pygame.K_RIGHT:
				right = False
			if event.key == pygame.K_UP:
				up = False
			if event.key == pygame.K_DOWN:
				down = False
				
	if up:
		Player.up()
	if down:
		Player.down()
	if left:
		Player.left()
	if right:
		Player.right()
	Player.checkOff()
	Player.draw(screen)
	pygame.display.flip()
pygame.quit()