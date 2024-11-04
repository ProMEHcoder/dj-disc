import pygame

pygame.init()

# make game window
Screen_width = 800
Screen_height = 600

screen = pygame.display.set_mode((Screen_width,Screen_height))

sownd = pygame.mixer.Sound("s.mp3")
s = pygame.mixer.Sound("a.mp3")
so = pygame.mixer.Sound("d.mp3")
sow = pygame.mixer.Sound("w.mp3")
sown = pygame.mixer.Sound("q.mp3")
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


	# make event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False



	pygame.display.update()
	pygame.time.Clock().tick(60)

pygame.quit()
