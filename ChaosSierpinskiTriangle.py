#Olivia Millard - Homework 3
#This program will generate a Sierpinski Triangle.

import pygame, random, math


## PRE- user-inputted width/height to generate the size of the image                            
## POST- Creates a list with (len(length[0])); each list item is a list with (len(size[1]))     
## Points = image[x][y]: 3 components = [0]: red; [1]: green; [2]: blue                        

def newImage(size):
    return pygame.surfarray.array3d(pygame.Surface(size))
                                                                                                 
## PRE- image is a list of list of 3-tuples; 3 tuple: (R, G, B)                                    
## POST- the image is displayed                                                                   

def showImage(image):
    width, height, depth = image.shape
    pygame.display.set_mode((width, height))
    surface = pygame.display.get_surface()
    pygame.surfarray.blit_array(surface, image)
    pygame.display.flip()


## This function will take width/height as values to generate random points in the image.
## It does not output anything.

def random_point(width, height):
    x_one = (random.random() * width)
    y_one = (random.random() * height)
    return(x_one, y_one)

## This function will find the midpoint between the randomly generated point within the window and the randomly generated corner.
## It does not output anything.

def midpoint(x_0, y_0, x_1, y_1):
    x_two = ((x_0 + x_1)/2)
    y_two = ((y_0 + y_1)/2)
    return x_two, y_two

## This function will color the triangle's points based off of a RGB colorscheme. 

def color_point (x, y, width, height):
    w = (255 / width)
    h = (255 / height)
    color_x = x * w
    color_y = y * h
    r = math.fabs(255 - color_y)
    g = math.fabs(255 - color_x)
    b = math.fabs(255 - color_x - color_y)
    return(r, g, b)

## This function will, first, get user-input to identify the width and height of the window.
## Next, this function will assign values to the three points of each triangle (p, c, m).

width = int(input("How wide would you like your window to be? "))
height = int(input("How tall would you like your window to be? "))
window = newImage((width, height))

for X in range(width):
    for Y in range(height):
        window[X][Y] = (255,255,255) 

p = 1
p = random_point(width, height)
i = 0
for i in range(4444444):
    img_corners = [(width, height),(0, height),(width // 2, 0)]
    c = random.choice(img_corners)
    m = midpoint(p[0], p[1], c[0], c[1])
    color = color_point((m[0]), (m[1]), width, height)
    if i > 20:
        window[(m[0])][(m[1])] = color 
        i = i + 1
    p = m
    if i % 1000 == 0:
        showImage(window)

pygame.init()

#To end the game.

print ('Done!')
input ("ENTER to quit")
pygame.quit()

