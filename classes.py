import math
import turtle
from turtle import *

# Define Physical Constants
G = 6.67428e-11         # Gravitational Constant
AU = 149.6e6 * 1000     # 1 AU, in meters
LY = 9.46e15            # 1 lightyear in meters
vSun = 230              # Velocity of the Sun, in km/s

class Star:
    
    def __init__(self, mass, radius, name=None):
        self.mass = mass            # Mass of star, kg
        self.radius = radius        # Radius of star, km
        if name is None:
            self.name = 'Unnamed star'
        else:
            self.name = name
        self.planets = []           # Planets orbiting star

        self.escapeVelocity = math.sqrt(2*G*self.mass/self.radius)

        
    def __str__(self):
        planets = ''
        for planet in self.planets:
            planets = planets + planet.name + ', '
        planets = planets[:-1]
        return(self.name +
               '\nMass: ' + '{:.2E}kg'.format(self.mass) + 
               '\nRadius: ' + '{:.2E}km'.format(self.radius) +
               '\nOrbiting Planets: ' + planets)
        
    def addPlanet(self, planet):
        self.planets += [planet]
        
class Planet:
    
    def __init__(self, mass, radius, star, distance, name=None):
        self.mass = mass            # Mass of planet, kg
        self.radius = radius        # Radius of planet, km
        self.star = star            # Star around which planet orbits
        self.distance = distance    # Orbital radius from star, km
        if name is None:
            self.name = 'Unnamed planet'
        else:
            self.name = name
        self.star.addPlanet(self)   # Add planet to list of plantets orbiting star
        
        # Escape and Orbital velocities, m/s
        self.escapeVelocity = math.sqrt(2*G*self.mass/(self.radius*1000))
        self.orbitalVelocity = math.sqrt(G*self.star.mass/(self.distance*1000))
        
        # Orbital Period, yr
        self.orbitalPeriod = self.distance*2*math.pi/self.orbitalVelocity/(3600*24*365.25)
        
    def __str__(self):
        return(self.name +
               '\nMass: ' + '{:.2E}kg'.format(self.mass) + 
               '\nRadius: ' + '{:.2E}km'.format(self.radius) +
               '\nOrbits Around: ' + self.star.name + 
               '\nOrbital Radius: ' + '{:.2E}km'.format(self.distance))

class Body(Turtle):

    name = 'Body'       # Name of body, initialized to 'Body'
    mass = 0            # Mass of body, initialized to zero kg
    xPosition = 0       # X component of body position, initialized to zero m
    yPosition = 0       # Y component of body position, initialized to zero m    
    xVelocity = 0       # X component of body velocity, initialized to zero m/s
    yVelocity = 0       # Y component of body velocity, initialized to zero m/s
    
    positions = []
    velocities = []
    forces = []
    
    def createRecords(self):
        self.positions  = [ [ ], [ ] ]      # [ xPositions,  yPositions  ]
        self.velocities = [ [ ], [ ] ]      # [ xVelocities, yVelocities ]
        self.forces     = [ [ ], [ ] ]      # [ xForces,     yForces     ]    
    
    # Returns the force exerted upon this body by the other body.
    def gravitationalForce(self, otherBody):     
        # Body does not exert a force on itself
        if self == otherBody:   
            raise ValueError('Attraction of object', self.name, 'to itself requested')

        # Find distance between otherBody and the body of interest
        deltaX = otherBody.xPosition - self.xPosition
        deltaY = otherBody.yPosition - self.yPosition
        distance = math.sqrt(deltaX**2 + deltaY**2)

        # If distance is zero, bodies have collided
        if distance == 0:
            raise ValueError('Collision between objects', self.name, 'and', otherBody.name)

        # Compute the gravitational force of the other body on the body of interest
        f_gravitational = G * self.mass * otherBody.mass / (distance**2)

        # Compute the direction of the force.
        theta = math.atan2(deltaY, deltaX)
        xForce = math.cos(theta) * f_gravitational
        yForce = math.sin(theta) * f_gravitational
        return xForce, yForce
    
''' The code for Body and simulate classes was written with the source code at
https://fiftyexamples.readthedocs.io/en/latest/gravity.html used as a guide. '''