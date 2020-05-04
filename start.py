import pygame
from  pygame.locals import *
from sys import exit
from random import randint
import sg1
import sg2

while True:
	op=2
	pygame.init()
	display=pygame.display.set_mode((800,600),0,24)#creates a window of appropriate sizw
	cap=pygame.display.set_caption( "THE DEADLY SNAKE")
	title=pygame.font.SysFont('comicsansms',50,True,True)
	title1=title.render("THE DEADLY SNAKE",True,(0,0,255))#to display the name of the game onto the screen
	clock=pygame.time.Clock()
	start=pygame.font.SysFont("comicsansms",50)
	text1=start.render("Press s to start",True,(0,0,255))
	end=pygame.font.SysFont("comicsansms",50)
	text2=end.render("Press q to exit",True,(0,0,255))

	pygame.draw.rect(display,(255,0,0),[400,200,20,20],0)#drawing the food
	display.blit(title1,(300,50))#to display one image onto another with the first operand as the source and second as its destination
	display.blit(text1,(50,350))
	display.blit(text2,(50,450))
	for i in [[560,120],[540,120],[520,130],[510,130],[500,140],[490,140],[480,150],[470,150],[460,160],[450,160],[440,170],[430,170],[420,180],[410,180],[400,190],[400,200]]:
		pygame.draw.rect(display,(0,255,0),Rect(i,[20,20]),0)
		pygame.display.flip()
		clock.tick(10)
	pygame.display.flip()
	#controls the start and the quit of the game
	while True:
		for i in pygame.event.get():
			if i.type==QUIT:
				exit()
		   	key1=pygame.key.get_pressed()#array of boolean values to show the status of the key on the keyboard
		   	if key1[K_q]:
		   	   exit()
		   	if key1[K_s]:
		   	   break
		if key1[K_s]:
		   	   break
		
	break
   
while True:

 press=pygame.key.get_pressed()
 for i in pygame.event.get():
  if i.type==QUIT:
	exit()
  key1=pygame.key.get_pressed()#array of boolean values to show the status of the key on the keyboard
  if key1[K_q]:
 	exit()
  if key1[K_s]:
  	break
  	
   
 display.fill((0,0,0))
 mousepress=pygame.mouse.get_pressed()
 l1=pygame.font.SysFont("comicsansms",50)
 l2=pygame.font.SysFont("comicsansms",30)
 l3=pygame.font.SysFont("comicsansms",30)
 l4=pygame.font.SysFont("comicsansms",35)
 r2=Rect((100,200),l2.size("Press 1 for Level 1 "))
 r3=Rect((100,250),l3.size("Press 2 for Level 2 "))
 display.blit(l1.render("Select Your Level",True,(0,0,255)),(100,100))
 display.blit(l2.render("Press 1 for Level 1 ",True,(0,0,255)),(100,200))
 display.blit(l3.render("Press 2 for level 2 ",True,(0,0,255)),(100,250))
 display.blit(l4.render("Game is originally in dark mode for light mode press L",True,(0,0,255)),(50,500))
 pygame.display.update()
 if press[K_l]:
	op=1  
 if press[K_1] or  (r2.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
  	sg2.game(op)
 if press[K_2] or  (r3.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
  	sg1.game(op)

 
  
  	
 
   	   



