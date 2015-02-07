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
		self.playerList = [pygame.image.load("images/cave.png"), pygame.image.load("images/character.png").convert_alpha(), pygame.image.load("images/character2.png").convert_alpha(),pygame.image.load("images/character3.png").convert_alpha(),pygame.image.load("images/character4.png").convert_alpha(),pygame.image.load("images/characterattack.png").convert_alpha()]
		self.enemyCostume = [pygame.image.load("images/enemy1.png").convert_alpha(), pygame.image.load("images/enemy2.png").convert_alpha()]
		self.enemies = []
		self.enemyLocationx = []
		self.enemyLocationy = []
		self.enemyHealth = []
		self.fireballs = [pygame.image.load("images/fire1.png").convert_alpha(),pygame.image.load("images/fire2.png").convert_alpha(),pygame.image.load("images/fire3.png").convert_alpha(),pygame.image.load("images/fire4.png").convert_alpha()]
		self.firelist = []
		self.firelocationx = []
		self.firelocationy = []
		self.firedirection = []
		self.coins = []
		self.coinx = []
		self.coiny = []
		self.healthbox = []
		self.healthy = []
		self.healthx = []

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
		self.font = pygame.font.Font(None,25)
		self.health = 5
		self.hurttimer = 500
		self.numofEnemies = 0
		self.enemynumber = 0
		self.checknum = 0
		self.checkcount = 0
		self.checkx = False
		self.checky = False
		self.attackx = False
		self.attacky = False
		self.enemymove = False
		self.movespot = -1
		self.attacktimer = 200
		self.attacking = False
		self.fireskin = 0
		self.fx = 0
		self.fy = 0
		self.firenum = 0
		self.deadcount = 0
		self.score = 0
		self.minimap1 = pygame.image.load("images/minimap.png")
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

		self.thelocation = 0

		
		self.hurttimer += .5
		self.attacktimer += 1
	def minimap(self):
		self.thingy = True


	def randomizer(self):
		self.randval = random.randrange(1,10)
		
		return self.randval
	def checkgotdrop(self):
		self.dropx = False
		self.dropy = False
		self.dropnum = 0
		for f in self.healthx:
			if f + 20 + self.playerx > self.characterx and f + 20 + self.playerx < self.characterx + 40:
				self.dropx = True
			if self.healthy[self.dropnum] + 20 + self.playery > self.charactery and self.healthy[self.dropnum] + 20 + self.playery < self.charactery + 60:
				self.dropy = True
			if self.dropy and self.dropx:
				self.healthy.pop(self.dropnum)
				self.healthx.pop(self.dropnum)
				self.healthbox.pop(self.dropnum)
				self.health += 1
				self.healthlimit()
			self.dropnum += 1
		self.dropx = False
		self.dropy = False
		self.dropnum = 0
		for f in self.coinx:
			if f + 20 + self.playerx > self.characterx and f + 20 + self.playerx < self.characterx + 40:
				self.dropx = True
			if self.coiny[self.dropnum] + 20 + self.playery > self.charactery and self.coiny[self.dropnum] + 20 + self.playery < self.charactery + 60:
				self.dropy = True
			if self.dropy and self.dropx:
				self.coiny.pop(self.dropnum)
				self.coinx.pop(self.dropnum)
				self.coins.pop(self.dropnum)
				
				self.score += 450
				self.dropnum += 1
	def healthlimit(self):
		if self.health > 5:
			self.health = 5
	def draw(self,aScreen):
		self.attacking = False
		self.firenumber = 0
		self.powernumber = 0
		aScreen.blit(self.playerList[0],(self.playerx,self.playery))
		self.enemynumber = 0
		for f in self.enemies:
				aScreen.blit(f,(self.enemyLocationx[self.enemynumber]+ self.playerx  , self.enemyLocationy[self.enemynumber]+ self.playery))
				self.enemynumber += 1
		aScreen.blit(self.playerList[self.costume],(self.characterx,self.charactery))

		pygame.draw.rect(aScreen, ((250,0,0)), (20,300,self.health * 30,40), 0)
		for f in self.firelist:
			aScreen.blit(f,(self.firelocationx[self.firenumber],self.firelocationy[self.firenumber]))
			self.firenumber += 1
		for f in self.firelist:
			self.attacking = True
		for f in self.coins:
			aScreen.blit(f,(self.coinx[self.powernumber] + self.playerx,self.coiny[self.powernumber] + self.playery))
			self.powernumber += 1
		self.powernumber = 0
		for f in self.healthbox:
			aScreen.blit(f,(self.healthx[self.powernumber] + self.playerx,self.healthy[self.powernumber] + self.playery))
			self.powernumber += 1
		self.scoretext = self.font.render(str(self.score),1,(255,255,255))
		aScreen.blit(self.scoretext,(10,10))
		self.minimap()
		aScreen.blit(self.minimap1,(400,300))
	def newEnemies(self):
		self.numofEnemies = 0
		self.numofEnemies = random.randint(50,100)
		self.checkcount = self.numofEnemies
		while self.numofEnemies > 0:
			self.x = random.randint(500,2400)
			self.y = random.randint(380,1800)
			
			self.enemyLocationx.append(self.x)
			self.enemyLocationy.append(self.y)
			self.enemies.append(self.enemyCostume[0])

			self.numofEnemies -= 1
	
	def attacks(self):
		
		if self.attacktimer > 300:
			self.attacktimer = 0
			self.fx = self.characterx
			self.fy = self.charactery + 30
			if self.firenum <= 0:
				if self.costume == 1:
					self.firelist.append(self.fireballs[0])
					self.firelocationx.append(self.fx)
					self.firelocationy.append(self.fy)
					self.firedirection.append(self.costume)
				if self.costume == 2:
					self.firelist.append(self.fireballs[1])
					self.firelocationx.append(self.fx)
					self.firelocationy.append(self.fy)
					self.firedirection.append(self.costume)
				if self.costume == 3:
					self.firelist.append(self.fireballs[2])
					self.firelocationx.append(self.fx)
					self.firelocationy.append(self.fy)
					self.firedirection.append(self.costume)
				if self.costume == 4:
					self.firelist.append(self.fireballs[3])
					self.firelocationx.append(self.fx)
					self.firelocationy.append(self.fy)
					self.firedirection.append(self.costume)
				
				self.firenum += 1
		self.deadcount = 0
		for f in self.firelist:
			self.deadcount += 1
	def firefly(self):
		self.fireplacement = 0
		for f in self.firedirection:
			if f == 1:
				self.firelocationx[self.fireplacement] -= .75

			if f == 2:
				self.firelocationx[self.fireplacement] += .75

			if f == 3:
				self.firelocationy[self.fireplacement] -= .75

			if f == 4:
				self.firelocationy[self.fireplacement] += .75
			
			self.fireplacement += 1

	def firecheck(self):
		self.thelocation = 0
		for f in self.firelocationx:
			if f > 480 or f < 0:
				self.firelocationx.pop(self.thelocation)
				self.firelist.pop(self.thelocation)
				self.firelocationy.pop(self.thelocation)
				self.firedirection.pop(self.thelocation)
				self.firenum -= 1
				self.attacking = False
			self.thelocation += 1
		self.thelocation = 0
		for f in self.firelocationy:
			if f > 360 or f < 0:
				self.firelocationy.pop(self.thelocation)
				self.firelist.pop(self.thelocation)
				self.firelocationx.pop(self.thelocation)
				self.firedirection.pop(self.thelocation)
				self.firenum -= 1
				self.attacking = False
			self.thelocation += 1

	def checkdead(self):
		self.deadx = False
		self.deady = False
		self.deadcount = 0
		if self.attacking:
			for f in self.enemyLocationx:
				if self.attacking:
					self.deadx = False
					self.deady = False
					if self.firelocationx[0] + 10 > f + self.playerx and self.firelocationx[0] + 10 < f + self.playerx + 40:
						self.deadx = True
					if self.firelocationy[0] + 10 > self.enemyLocationy[self.deadcount] + self.playery and self.firelocationy[0] + 10 < self.enemyLocationy[self.deadcount] + 60 + self.playery:
						self.deady = True

					if self.deadx and self.deady:
						self.score += 100
						self.newthing = self.randomizer()
						if self.newthing == 1 or self.newthing == 2 or self.newthing == 10:
							self.coins.append(pygame.image.load("images/coin.png").convert_alpha())
							self.coinx.append(self.enemyLocationx[self.deadcount] )
							self.coiny.append(self.enemyLocationy[self.deadcount] )

						if self.newthing == 3:
							self.healthbox.append(pygame.image.load("images/health.png").convert_alpha())
							self.healthx.append(self.enemyLocationx[self.deadcount] )
							self.healthy.append(self.enemyLocationy[self.deadcount] )
						self.firelocationx.pop(0)
						self.firelist.pop(0)
						self.firelocationy.pop(0)
						self.firedirection.pop(0)
						self.enemyLocationy.pop(self.deadcount)
						self.enemyLocationx.pop(self.deadcount)
						self.enemies.pop(self.deadcount)
						self.attacking = False
						self.checkcount -= 1
						self.firenum -= 1
					self.deadcount += 1
	


	def left(self):

		if self.walkx:
			self.characterx -= .3
			self.costume = 1
			
		if self.scrollx:
			self.playerx += .3
			self.costume = 1

		
				

	def right(self):
		if self.walkx:
			self.characterx += .3
			self.costume = 2
		
		if self.scrollx:
			self.playerx -= .3
			self.costume = 2
		
	
				
	def up(self):
		if self.walky:
			self.charactery -= .3
			self.costume = 3
		

		if self.scrolly:
			self.playery += .3
			self.costume = 3
			
		
				
	def down(self):
		if self.walky:
			self.charactery += .3
			self.costume = 4

		
		if self.scrolly:
			self.playery -= .3
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

			

			if self.checkx and self.checky:
				self.healthtime()
				self.checkx = False
			self.checkx = False
			self.checky = False
			self.checknum += 1
	def attack(self):
		self.attackx = False
		self.attacky = False
		self.checknum = 0
		while self.checknum < self.checkcount:
			if self.enemyLocationx[self.checknum] + self.playerx > 0 and self.enemyLocationx[self.checknum] + self.playerx < 480:
				self.attackx = True

			if self.enemyLocationy[self.checknum] + self.playery > 0 and self.enemyLocationy[self.checknum] + self.playery < 360:

				self.attacky = True

			if self.attackx and self.attacky:
				if self.enemyLocationx[self.checknum] + self.playerx  > self.characterx:
					self.enemyLocationx[self.checknum] -= .25 
					

				if self.enemyLocationx[self.checknum] + self.playerx  < self.characterx:
					self.enemyLocationx[self.checknum] += .25
					
				if self.enemyLocationy[self.checknum] + self.playery > self.charactery:
					self.enemyLocationy[self.checknum] -= .25
					
				if self.enemyLocationy[self.checknum] + self.playery < self.charactery:
					self.enemyLocationy[self.checknum] += .25
					
			self.attackx = False
			self.attacky = False
			self.checknum += 1

			
			
attack1 = False			
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
			if event.key == pygame.K_z:
				attack1 = True
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				left = False
			if event.key == pygame.K_RIGHT:
				right = False
			if event.key == pygame.K_UP:
				up = False
			if event.key == pygame.K_DOWN:
				down = False
	if attack1:
		Player.attacks()
		attack1 = False

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
	Player.attack()
	Player.firefly()
	Player.firecheck()
	Player.checkdead()
	Player.checkgotdrop()
	Player.draw(screen)
	
	pygame.display.flip()

pygame.quit()