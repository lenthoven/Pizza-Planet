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
		self.enemyCostume = [pygame.image.load("images/enemy1.png").convert_alpha(), pygame.image.load("images/enemy2.png").convert_alpha()]
		self.enemies = []
		self.enemyLocationx = []
		self.enemyLocationy = []
		self.x = 0
		self.y = 0
		self.playerx = 0
		self.playery = 0
		self.characterx = 220
		self.charactery = 150
		self.move = 0
		self.scrollx = True
		self.scrolly = True
		self.costume = 1
		self.stateChange = True
		self.walkx = True
		self.walky = True
		self.part1 = False
		self.part2 = False
		self.font = pygame.font.Font(None,500)
		self.health = 5
		self.hurttimer = 500
		self.numofEnemies = 0
		self.enemynumber = 0
		self.checknum = 0
		self.checkcount = 0
		self.checkx = False
		self.checky = False
	def checkOff(self):
		
		if self.characterx > 219 and self.characterx < 221:
			self.scrollx = True
			self.walkx = False
			self.part1 = True
			
		if self.charactery > 149 and self.charactery < 151:
			self.scrolly = True
			self.walky = False
			self.part2 = True
				
		
			

		if self.playerx < 0 and self.playerx > -1920:
			self.scrollx = True
			self.walkx = False

			self.stateChange = False
			self.part1 = False
			self.part2 = False


		if self.playery < 0 and self.playery > -1440:
			self.scrolly = True
			self.walky = False

			self.stateChange = False
			self.part1 = False
			self.part2 = False


		if self.playerx > 0 or self.playerx < -1920:
			if self.playerx > 0:
				self.playerx = 0

			if self.playerx < -1920:
				self.playerx = -1920
			self.scrollx = False
			self.walkx = True
			self.stateChange = True


		if self.playery > 0 or self.playery < -1440:
			if self.playery > 0:
				self.playery = 0

			if self.playery < -1440:
				self.playery = -1440
			self.scrolly = False
			self.walky = True
			self.stateChange = True


		if self.characterx >= 440 or self.characterx <= 0:
			if self.characterx >= 440:
				self.characterx = 440
				

			if self.characterx <= 0:
				self.characterx = 0
				


		if self.charactery >= 300 or self.charactery <= 0:
			if self.charactery >= 300:
				self.charactery = 300
				

			if self.charactery <= 0:
				self.charactery = 0
				



		if self.health <= 0:
			self.health = 0
			return self.health

		self.hurttimer += .5
		
	def draw(self,aScreen):
		

		aScreen.blit(self.playerList[0],(self.playerx,self.playery))
		self.enemynumber = 0
		for f in self.enemies:
				aScreen.blit(f,(self.enemyLocationx[self.enemynumber]+ self.playerx  , self.enemyLocationy[self.enemynumber]+ self.playery))
				self.enemynumber += 1
		aScreen.blit(self.playerList[self.costume],(self.characterx,self.charactery))

		pygame.draw.rect(aScreen, ((250,0,0)), (20,300,self.health * 30,40), 0)
		


	def newEnemies(self):
		self.numofEnemies = 0
		self.numofEnemies = random.randint(10,20)
		self.checkcount = self.numofEnemies
		while self.numofEnemies > 0:
			self.x = random.randint(0,2400)
			self.y = random.randint(0,1800)
			
			self.enemyLocationx.append(self.x)
			self.enemyLocationy.append(self.y)
			self.enemies.append(self.enemyCostume[0])

			self.numofEnemies -= 1
	
	
			

	def left(self):

		if self.walkx:
			self.characterx -= .1
			self.costume = 1
			
		if self.scrollx:
			self.playerx += .1
			self.costume = 1

		
				

	def right(self):
		if self.walkx:
			self.characterx += .1
			self.costume = 2
		
		if self.scrollx:
			self.playerx -= .1
			self.costume = 2
		
	
				
	def up(self):
		if self.walky:
			self.charactery -= .1
			self.costume = 3
		

		if self.scrolly:
			self.playery += .1
			self.costume = 3
			
		
				
	def down(self):
		if self.walky:
			self.charactery += .1
			self.costume = 4

		
		if self.scrolly:
			self.playery -= .1
			self.costume = 4
			
	def healthtime(self):
		if self.hurttimer > 500:
				self.health -= 1
				self.hurttimer = 0
		

	def checkHit(self):
		self.checkx = False
		self.checky = False
		self.checknum = 0
		while self.checknum < self.checkcount:
			if self.enemyLocationx[self.checknum] + self.playerx < self.characterx + 20 and self.enemyLocationx[self.checknum] + 40 + self.playerx > self.characterx:
				self.checkx = True

			if self.enemyLocationy[self.checknum] + self.playery < self.charactery + 30 and self.enemyLocationy[self.checknum] + 60 + self.playery > self.charactery:
				self.checky = True

			self.checknum += 1

			if self.checkx and self.checky:
				self.healthtime()
			self.checkx = False
			self.checky = False

			
			
			
				
Player = Player()
Player.newEnemies()
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
	healthy = Player.checkOff()
	if healthy == 0:
		running = False
	Player.checkHit()
	Player.draw(screen)
	
	pygame.display.flip()

pygame.quit()