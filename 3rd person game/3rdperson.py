import pygame
import random
up = False
down = False
right = False
left = False
class Player:
	def __init__(self):
		self.playerList = [pygame.image.load("images/cave.png")]
		self.playerx = -600
		self.playery = -450
		self.move = 0
	def checkOff(self):
		self.move = 10
	def draw(self,aScreen):
		aScreen.blit(self.playerList[0],(self.playerx,self.playery))
	def left(self):
		self.playerx += 20
	def right(self):
		self.playerx -= 20
	def up(self):
		self.playery += 20
	def down(self):
		self.playery -= 20

		
Player = Player()
screen = pygame.display.set_mode((1200,900))
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
	Player.draw(screen)
	pygame.display.flip()
pygame.quit()