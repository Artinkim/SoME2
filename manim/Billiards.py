import numpy as np
import pygame
import time
import random
import math

#default = True
particleCount = 1000
screenDimension = 800,800
staringRange = 0,screenDimension[0],0,screenDimension[1]
infinteTrail = False
integerCord = False
minVelocity = 1.25
maxVelocity = 1.26
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

#images = [pygame.image.load(i+".png") for i in range(15)]

#screenDimension = 1920,1080

if integerCord:
    minVelocity = int(math.ceil(minVelocity))
    maxVelocity = int(math.floor(maxVelocity))

particlesX = np.random.uniform(0,5,size=particleCount)
particlesY = np.random.uniform(0,5,size=particleCount)
particlesPos = np.stack((particlesX, particlesY), axis = -1)
particlesVelocity = np.random.uniform(minVelocity,maxVelocity,size=(particleCount,2))
particles = np.hstack((particlesPos, particlesVelocity))
particleColors = np.random.randint(0,255,size=(particleCount,3))


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
    pygame.draw.circle(screen,(255,255,255),(screenDimension[0]/2,screenDimension[1]/2),100)
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
                
                
        #THIS IS THE PARTICLE         
        xdiff = particles[i][0]-screenDimension[0]/2
        ydiff = particles[i][1]-screenDimension[1]/2
        distance2center =(xdiff**2+ydiff**2)**(1/2)
        if distance2center < 100:
            #THIS CHECK FOR COLLISION WITH THE CENTER CIRCLE
            magnitude = (particles[i][2]**2+particles[i][3]**2)**(1/2)
            
            theta_0=math.atan2(ydiff, xdiff)
            theta_1=math.atan2(-particles[i][3], -particles[i][2])

            theta_3=2*(theta_0-theta_1)

            new_vx=magnitude*math.cos(theta_3)
            new_vy=magnitude*math.sin(theta_3)
            
            particles[i][2]=new_vx
            particles[i][3]=new_vy
            particles[i][0] = (100)*math.cos(theta_0)+screenDimension[0]/2
            particles[i][1] = (100)*math.sin(theta_0)+screenDimension[1]/2
            
            
            
        pygame.draw.circle(screen,particleColors[i],particles[i][0:2],partilceSize)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # if r key gets pressed reset all particles positions to 0,0
        keys=pygame.key.get_pressed()
        if keys[pygame.K_r]:
            for i in range(particleCount):
                particles[i][0] = np.random.rand()
                particles[i][1] = np.random.rand()
    pygame.display.update()
    clock.tick(tickRate)

    if verbose:
        tmp = time.time()-start
        if tmp > 0:
            print(1/tmp)
