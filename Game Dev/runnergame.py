import pygame #Imports pygame module.
from sys import exit #Imports only one function from sys module.

pygame.init() #Initializes all pygame modules, so always start program with this line.
screen = pygame.display.set_mode((800, 400)) #Creates a display surface which must be stored in a variable. The dimensions of the display are in a (width, height) format. The code ended here so we only saw the screen for a short second.
pygame.display.set_caption("Runner Game") #Creates a caption for the display surface - essentially the window's title.
clock = pygame.time.Clock() #Creates a clock object - essentially what keeps the game running at a certain framerate (ish).
test_font = pygame.font.Font('Game Dev/Font/Pixeltype.ttf', 50) #Creates a font. Arguements in oder (font type, font size)

sky_surface = pygame.image.load('Game Dev/Graphics/runner game sky image.png').convert() #This is a new surface, and so has its own separate graphical inputs.
ground_surface = pygame.image.load('Game Dev/Graphics/runner game ground image.png').convert() #This regular surface follows the same (w,h) dimentions. (0,0) hides this surface.
sprite_surface = pygame.image.load('Game Dev/Graphics/spritesheet.png').convert_alpha() #Convert_alpha() retains transparency and boost performance.

score_surface = test_font.render("Runner Game", False, (64, 64, 64)) #Renders the text. Arguements follow the order (text info, of/off anti aliasing, colour). Im using an RGB tuple.
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('Game Dev/Graphics/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('Game Dev/Graphics/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomright = (80, 300)) #Creates a rectangle for the player, with the focus point at the middle bottom of the image. You can now align the player with the ground easily, and introduce collisions. A sprite merges a surface and a rect, and this will be shown later. Moving any point of the rectangle will move the rest of the points so they're position is relative to each other. 

while True: #This is the main game loop, which runs until the user exits. This will also display our display surface.
    for event in pygame.event.get(): #Gets us the events.
        if event.type == pygame.QUIT: #Checks if the user has clicked the x close button on the window.
            pygame.quit() #Quits the program by uninitializing all pygame modules. However, this is the opposite of pygame.init(), so the window cant be run once pygame.quit is up. The while loop must be 'broken'.
            exit() #Exits the program and ends the while true loop to prevent error message. 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Jump.")


    screen.blit(sky_surface,(0,0))#Order of images follows order of code, so what is executed first is behind the second. 
    screen.blit(ground_surface,(0,300)) #Block image transfer - allows the regular test surface to be put on the display surface. Uses coords, with 0,0 at the TOP LEFT CORNER. Width goes right, height goes down.
    pygame.draw.rect(screen, '#c0e8ec', score_rect) #pygame.draw is telling pygame to draw something, and the rect specifies we want a rectangle shape. Border rounding, width etc are more arguements avaiable. 
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface, score_rect)
    
    snail_rect.x -= 4
    if snail_rect.right < 0: #Right side of the snail is at 0, meaning the snail image is all gone, so the snail must be 'looped back'
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect) #The previous snails don't disappear, so without the refreshing background, the snail image 'stretches'.
    screen.blit(player_surface, player_rect)

    # keys = pygame.key.get_pressed() #Stores the check for whether a key was pressed. Boolean so 0 means is not pressed, 1 means is pressed.
    # keys[pygame.K_SPACE] #Specifically checks if a space key was pressed as it checks the array created by above function. This can all be done in the event loop.

    # if player_rect.colliderect(snail_rect): #Checks if 2 rects have collided. Boolean so this outputs either 0 ot 1 (f/t). Pygame checks every single frame though. Collide point is used for mouse interactions.
    #    print("Collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #   print(pygame.mouse.get_pressed())

    pygame.display.update() #This updates the display surface.
    clock.tick(60) #Tells the computer that this while loop must run more than 60 times /s, aka fps ceiling. Fps floor cannot be set; the code can only be optimized

