import pygame

pygame.init()

# make game window
Screen_width = 800
Screen_height = 600

screen = pygame.display.set_mode((Screen_width,Screen_height))

# variables
sownd = pygame.mixer.Sound("s.mp3")
s = pygame.mixer.Sound("a.mp3")
so = pygame.mixer.Sound("d.mp3")
sow = pygame.mixer.Sound("w.mp3")
sown = pygame.mixer.Sound("q.mp3")
sownm = pygame.mixer.Sound("e.mp3")
sownma = pygame.mixer.Sound("z.mp3")
sownmak = pygame.mixer.Sound("x.mp3")
sownmake = pygame.mixer.Sound("c.mp3")
#backdrop
bgs=pygame.image.load("back.jpg")
bgs=pygame.transform.scale(bgs,(Screen_width,Screen_height))
bg=bgs.get_rect()
# make game loop
run = True
while run:
	

	key = pygame.key.get_pressed()
	if key[pygame.K_s] == True:
  		pygame.mixer.Sound.play(sownd)
	if key[pygame.K_a] == True:
  		pygame.mixer.Sound.play(s)
	if key[pygame.K_d] == True:
  		pygame.mixer.Sound.play(so)
	if key[pygame.K_w] == True:
  		pygame.mixer.Sound.play(sow)
	if key[pygame.K_q] == True:
  		pygame.mixer.Sound.play(sown)
	if key[pygame.K_e] == True:
  		pygame.mixer.Sound.play(sownm)
	if key[pygame.K_z] == True:
  		pygame.mixer.Sound.play(sownma)
	if key[pygame.K_x] == True:
  		pygame.mixer.Sound.play(sownmak)
	if key[pygame.K_c] == True:
  		pygame.mixer.Sound.play(sownmake)

  	# background
	screen.blit(bgs,bg)

	# make event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False



	pygame.display.update()
	pygame.time.Clock().tick(60)

pygame.quit()
