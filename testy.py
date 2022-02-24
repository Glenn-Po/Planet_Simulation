
import pygame
import math

pygame.init()


#[GUI CONSTANTS]
FPS = 30
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
MARGIN = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (80, 100, 255)
LIGHTBLUE = (0, 0, 125)

RED = (125, 50, 50)


def offseter(x, y):
    return (x + WINDOW_WIDTH/2 , y+WINDOW_HEIGHT/2)


#[Planet Constants]


AU = 149.597870e6 * 1000 #ie in meters
G = 6.67428e-11
SCALE = 250*.5 / AU
S = 250000*2/ AU
TIME_STEP = 24
SR = 6.96e8
class Planet(object):
    

    def __init__(self, mass, radius, color, distanceToSun):
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbitalPoints= []

        self.distanceToSun = distanceToSun + SR

#scal first
    def getPosition(self, time):
        teta = (math.sqrt(G*self.mass
                          / self.radius)/self.radius)*time

        x = SCALE*(self.distanceToSun)*math.cos(teta) + WINDOW_WIDTH//2
        y = SCALE*(self.distanceToSun)*math.sin(teta)+ WINDOW_HEIGHT//2 
        self.orbitalPoints.append((x,y))
        return (x, y)


#1 au = 100px
class Simulator:

    def __init__(self, planets):
        self.sun = {
            "mass": 1.98892e30,
            "radius": 6.96e8,
            "color": YELLOW,
            }
        self.planets = planets

        self.init()

    def init(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Planet Simulation")

    def drawPlanets(self, time):
        
        for planet in self.planets:
            if len(planet.orbitalPoints)>=3:
                pygame.draw.lines(self.window, planet.color, False, planet.orbitalPoints, 2)

            x, y = planet.getPosition(time)
            #pygame.draw.line(self.window, planet.color, ((WINDOW_WIDTH/2, WINDOW_HEIGHT/2)), (x, y))
            pygame.draw.circle(self.window, planet.color, (x, y), planet.radius*S)
            #calculate and display distance to sun
        

    def drawSun(self):
        radius = S*.1* self.sun["radius"]
        center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        pygame.draw.circle(self.window, YELLOW, center, 30)

    def runsimulation(self):
        running = True
        clock = pygame.time.Clock()
        time = 0
        self.window.fill(WHITE)
        while running:
            self.window.fill(WHITE)
            self.drawSun()
            self.drawPlanets(time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            #self.window.blit(self.window)
            # pygame.display.update()
            # pygame.time.wait(1000)

            pygame.display.update()
            clock.tick(FPS)
            time += (TIME_STEP)

        #add option for person to ask if they really want to quit
        pygame.quit()


#testing#

if __name__ == "__main__":

    #mass, radius, color, distance
    mercury = Planet(.33e24, (4879/2)*1000, RED, 57.9e6*1000)
    venus = Planet(4.87e24, (12104/2)*1000, YELLOW, 108.2e6*1000)
    earth = Planet(5.97e24, (12756/2)*1000, BLUE, 149.6e6*1000)
    mars = Planet(.642e24, (6792/2)*1000, LIGHTBLUE, 228e6*1000)
    
    jupiter = Planet(1898e24, (142984/2)*1000, RED, 778.5e6*1000)
    saturn =Planet(568e24, (120536/2)*1000, RED, 1432e6*1000)
    uranus = Planet(86.8e24, (51118/2)*1000, RED, 2867e6*1000)
    neptune = Planet(102e24, (49528/2)*1000, RED, 4515e6*1000)
    pluto = Planet(0.013e24, (2376/2)*1000, RED, 5906.4e6*1000)
    
    Simulator([mercury, venus, earth, mars ]).runsimulation()

