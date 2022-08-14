#Be able to have sliders and check boxes for parameters
#Move towards/with mouse movement
#!Connect with line of different strength depending on distance
#When bump into eachother reflect
#When bump into eachother change colors and mix colors (both become average of two colors)
#When bump into eachother merge to become bigger
#!Control size of particles
#Control directions particles come from
#Control acceleration of particles
#Multi Dimension
#!Bounce off walls
#Trail Time

# import os
# os.system("pip install numpy")
# os.system("pip install pygame")

import numpy as np
import pygame
import time
import random
import math

#default = True
particleCount = 6
screenDimension = 800,500
staringRange = 0,screenDimension[0],0,screenDimension[1]
infinteTrail = False
integerCord = False
minVelocity = 1.25
maxVelocity = 5
# screenFill = True
reflect = True
verbose = False
partilceSize = 5
lineSize = 1
tickRate = 100
lineDist = 100
dynamicLineBrightness = True
variableLineColor = True
staticColor = 0,255,0

partilceSizeH = partilceSize//2
staticColor = np.array(staticColor,dtype=np.uint8)


if integerCord:
    minVelocity = int(math.ceil(minVelocity))
    maxVelocity = int(math.floor(maxVelocity))

particlesX = np.random.uniform(staringRange[0],staringRange[1],size=particleCount)
particlesY = np.random.uniform(staringRange[2],staringRange[3],size=particleCount)
particlesPos = np.stack((particlesX, particlesY), axis = -1)
particlesVelocity = np.random.uniform(minVelocity,maxVelocity,size=(particleCount,2))
particles = np.hstack((particlesPos, particlesVelocity))
particleColors = np.random.randint(0,255,size=(particleCount,3))
# if variableLineColor:
#     particleColorsBright = np.empty((particleCount,3),dtype=np.uint8)
#     for i in range(particleCount):
#         increase = np.max(particleColors[i][:])
#         particleColorsBright[i] = (particleColors[i][:]+255-increase)
#     print(particleColorsBright)
#     particleColorsBright = particleColorsBright//2
#     print(particleColorsBright)
#     particleColorAverages = np.empty((particleCount,particleCount,3),dtype=np.uint8)
#     print(particleColorAverages.nbytes)
#     for i in range(particleCount):
#         particleColorAverages[i] = np.add(particleColorsBright,particleColorsBright[i])
# if integerCord:
#     particles = particles.astype("int16")


black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode(screenDimension)
screen.fill(black)
clock = pygame.time.Clock()
r = np.arange(particleCount)
if verbose:
    count = 0
    it = -10
while True:
    start = time.time()
    screen.fill(black)
    sortedX = np.sort(particles[:][0])
    sortedY = np.sort(particles[:][1])
    sortX = np.argsort(particles[:][0])
    sortY = np.argsort(particles[:][1])
    neighbors = np.array([(np.searchsorted(sortedX,i[0]-lineDist),np.searchsorted(sortedX,i[0]+lineDist),np.searchsorted(sortedY,i[1]-lineDist),np.searchsorted(sortedY,i[1]+lineDist)) for i in particles])
    neighbors = np.array([np.concatenate([sortX[a:b],sortY[c:d]]) for a,b,c,d in neighbors])
    for i in range(particleCount):

        particles[i][0]+=particles[i][2]
        particles[i][1]+=particles[i][3]
        if int(particles[i][0]) < 0 or int(particles[i][1]) < 0 or int(particles[i][0]) > screenDimension[0]-1 or int(particles[i][1]) > screenDimension[1]-1:
            if not reflect:
                tmp = random.choice([(0,random.random()*(screenDimension[1]-2)+1),
                (screenDimension[0]-1,random.random()*(screenDimension[1]-2)+1),
                (random.random()*(screenDimension[0]-2)+1,0),
                (random.random()*(screenDimension[0]-2)+1,screenDimension[1]-1)])
                particles[i][0] = tmp[0]
                particles[i][1] = tmp[1]

            if particles[i][0] <= 0:
                particles[i][2] = abs(particles[i][2])
                particles[i][0] = 0
            elif particles[i][0] >= screenDimension[0]-1:
                particles[i][2] = -abs(particles[i][2])
                particles[i][0] = screenDimension[0]-1
            if particles[i][1] <= 0:
                particles[i][3] = abs(particles[i][3])
                particles[i][1] = 0
            elif particles[i][1] >= screenDimension[1]-1:
                particles[i][3] = -abs(particles[i][3])
                particles[i][1] = screenDimension[1]-1

        pygame.draw.circle(screen,particleColors[i],particles[i][0:2],partilceSize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(tickRate)

    if verbose:
        tmp = time.time()-start
        if tmp > 0:
            print(1/tmp)
