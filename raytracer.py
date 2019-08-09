import pygame as pg  
import numpy as np
import random

# create a 3D array with 600x600x3 (the last dimension is for the RGB color)
cells = np.ndarray((480, 320, 3)) 

# color dictionary, represents white, red and blue
color_dict = {
        0: (255, 255, 255), 
        1: (255, 0, 0),
        2: (0, 0, 255)
        }

# pick a random color tuple from the color dict
for i in range(cells.shape[0]):
    for j in range(cells.shape[1]):
        cells[i][j] = color_dict[random.randrange(3)]

# set the size of the screen as multiples of the array
cellsize = 1
WIDTH = cells.shape[0] * cellsize 
HEIGHT = cells.shape[1] * cellsize

# initialize pygame
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

#create a surface with the size as the array 
surf = pg.Surface((cells.shape[0], cells.shape[1]))
 # draw the array onto the surface 
pg.surfarray.blit_array(surf, cells)
# transform the surface to screen size
surf = pg.transform.scale(surf, (WIDTH, HEIGHT)) 

# game loop
running, i = True, -1
print(cells.shape[0] )
print(cells.shape[1] )
 
while running: 
    #clock.tick(3000)
    if(i < HEIGHT-1):
        i +=1
    else:
        i =0 
    print(i) 
 

    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            running = False

    # for all         
    for k in range(cells.shape[0]):
        cells[k][i] = color_dict[random.randrange(3)]

    # update screen with pixel array        
    pg.surfarray.blit_array(surf, cells)    
    screen.fill((0, 0, 0))

    # blit the transformed surface onto the screen
     # draw the array onto the surface 

    screen.blit(surf, (0, 0)) 

    pg.display.update() 

pg.quit()