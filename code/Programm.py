# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
scr = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

# import files
pic_1 = pygame.image.load("bild1.jpg").convert()
pic_2 = pygame.image.load("bild2.jpg").convert()

cou_1 = pygame.image.load("1.jpg").convert()
cou_2 = pygame.image.load("2.jpg").convert()
cou_3 = pygame.image.load("3.jpg").convert()

# creating a running loop
while True:

    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:

            # checking if key "A" was pressed
            if event.key == pygame.K_ESCAPE:
                print("Key A has been pressed")
                pygame.quit()
                sys.exit()


            # checking if key "a" was pressed
            if event.key == pygame.K_a:
                print("Key a has been pressed")
                scr.blit(pic_1, (0,0))
                pygame.display.update()

            # checking if key "b" was pressed
            if event.key == pygame.K_b:
                print("Key b has been pressed")
                scr.blit(pic_2, (0,0))
                pygame.display.update()

            # checking if key "c" was pressed
            if event.key == pygame.K_c:
                print("Key c has been pressed")
                
                
            if event.key == pygame.K_1:
                print("Key P has been pressed")
                scr.blit(cou_1, (0,0))
                pygame.display.update()
                
            if event.key == pygame.K_2:
                print("Key P has been pressed")
                scr.blit(cou_2, (0,0))
                pygame.display.update()
            
            if event.key == pygame.K_3:
                print("Key P has been pressed")
                scr.blit(cou_3, (0,0))
                pygame.display.update()
