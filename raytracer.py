import pygame as pg   
import numpy as np
import random


HEIGHT = 320
WIDTH = 480
# set the size of the screen as multiples of the array
cellsize = 1
SCREEN_HEIGHT = HEIGHT * cellsize 
SCREEN_WIDTH = WIDTH * cellsize

# create a 3D array with HxWx3 (the last dimension is for the RGB color)
pixel_array = np.ndarray((HEIGHT, WIDTH, 3)) 

# color dictionary, represents white, red and blue
color_dict = { 
        0: (255, 255, 255),  
        1: (0, 255, 0),
        2: (0, 0, 255)
        } 

# pick a random color tuple from the color dict
for i in range(HEIGHT):
    for j in range(WIDTH): 
        pixel_array[i][j] = color_dict[random.randrange(3)]

# Initialize pygame
pg.init() 

# Initialize the screen for displaying pixels
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("PyR̶A̶Y̶")
pg.display.set_icon(pg.image.load("icon2.png")) 

# Clock for limiting framerate of window
clock = pg.time.Clock()

# Create a surface with the size as the array 
surf = pg.Surface((WIDTH, HEIGHT))
# copy values from pixel array onto the surface  
# (since mapping is inverted used a transpose
pg.surfarray.blit_array(surf, pixel_array.transpose(1,0,2))   

# Scale the surface to thescreen size
surf = pg.transform.scale(surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
# game loop
running, i = True, -1 

# Print all surface sizes  
print(f"Array: {HEIGHT} x {WIDTH}")
print(f"Surface: {surf.get_height()} x {surf.get_width()}")
print(f"Screen: {SCREEN_HEIGHT} x {SCREEN_WIDTH}")

while running: 
    # maximum 90 FPS 
    clock.tick(90)
      
    if(i < HEIGHT - 2):   
        i += 2
    else:
        i = 0   
 
 
    # Process quit event, if queried
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            running = False

    # for all width elements of line (process 2 lines at a time)         
    for j in range(WIDTH):
        pixel_array[i][j] = color_dict[random.randrange(3)]
        pixel_array[i-1][j] = color_dict[random.randrange(3)]

    # update screen with pixel array        
    pg.surfarray.blit_array(surf, pixel_array.transpose(1,0,2))    
    screen.fill((0, 0, 0))

    # blit the transformed surface onto the screen
    # draw the array onto the surface  

    screen.blit(surf, (0, 0)) 

    pg.display.update() 

pg.quit()