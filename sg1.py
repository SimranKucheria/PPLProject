import pygame
import random
import time

pygame.init()
def game(op):
	if op == 1:
		black=(0,0,0)
		white = (255, 255, 255)
	if op == 2:
		white=(0,0,0)
		black = (255, 255, 255)
	blue=(0,0,255)
	red=(255,0,0)
	yellow = (255, 255, 102)
	green = (0, 255, 0)
	display=pygame.display.set_mode((640,480))
	pygame.display.set_caption('Snake game')
	clock=pygame.time.Clock()
	game_exit=False
	game_lose = False
	
	x1=400
	y1=300

	x2=0
	y2=0

	snake_List = []
    	Length_of_snake = 1

	x3=round(random.randrange(0,640-20)/10.0)*10.0
	y3=round(random.randrange(0,480-20)/10.0)*10.0
		
	while not game_exit:
		while game_lose==True:
			display.fill(white)
			pygame.draw.line(display,green,(0,0),(0,480),20)
   			pygame.draw.line(display,green,(0,0),(640,0),20)
   			pygame.draw.line(display,green,(640,0),(640,480),20)
   			pygame.draw.line(display,green,(0,480),(640,480),20)
            		mesg = pygame.font.SysFont("bahnschrift", 25).render("You Lost! Press C-Play Again or Q-Quit", True, red)
	    		display.blit(mesg, [120, 250])
	    		value = pygame.font.SysFont("comicsansms", 35).render("Your Score: " + str(Length_of_snake-1), True, yellow)
    	    		display.blit(value, [200, 200])

            		pygame.display.update()
 
            		for event in pygame.event.get():
                		if event.type == pygame.KEYDOWN:
                    			if event.key == pygame.K_q:
                        			game_exit = True
                        			game_lose = False
                    		if event.key == pygame.K_c:
                        		game(op)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				game_exit=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x2=-10
					y2=0
				elif event.key==pygame.K_RIGHT:
					x2=+10
					y2=0
				elif event.key==pygame.K_UP:
					x2=0
					y2=-10
				elif event.key==pygame.K_DOWN:
					x2=0
					y2=+10

		if (x1>=640 or x1<0 or y1>=480 or y1 <0):
			game_lose=True
		x1+=x2
		y1+=y2	
		display.fill(white)	
		pygame.draw.line(display,green,(0,0),(0,480),20)
   		pygame.draw.line(display,green,(0,0),(640,0),20)
   		pygame.draw.line(display,green,(640,0),(640,480),20)
   		pygame.draw.line(display,green,(0,480),(640,480),20)
		#pygame.display.flip()
	
		pygame.draw.rect(display,red, [x3, y3, 20, 20])		
		snake_Head = []
        	snake_Head.append(x1)
        	snake_Head.append(y1)
        	snake_List.append(snake_Head)
        	if len(snake_List) > Length_of_snake:
            		del snake_List[0]
 
        	for x in snake_List[:-1]:
            		if x == snake_Head:
                		game_lose = True
 
	        for x in snake_List:
	        	pygame.draw.rect(display, black, [x[0], x[1], 20, 20])	
	        value = pygame.font.SysFont("comicsansms", 35).render("Your Score: " + str(Length_of_snake-1), True, red)
	    	display.blit(value, [15, 15])
 
	        pygame.display.update()
		
		if x1 == x3 and y1 == y3:
			x3=round(random.randrange(0,640-20)/10.0)*10.0
			y3=round(random.randrange(0,480-20)/10.0)*10.0
	   		Length_of_snake += 1
         
		clock.tick(15)
	pygame.quit()
	quit()
