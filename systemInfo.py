import numpy as np
from classes import *

# Create the Sun and its planets
sun = Star(1.9891e30, 695500, 'The Sun')
mercury = Planet(.330e24,4879/2,sun,57.9e6,'Mercury')
venus = Planet(4.87e24,12104/2,sun,108.2e6,'Venus')
earth = Planet(5.97e24,12756/2,sun,149.6e6,'Earth')
mars = Planet(0.642e24,6792/2,sun,227.9e6,'Mars')
jupiter = Planet(1898e24,142984/2,sun,778.6e6,'Jupiter')
saturn = Planet(568e24,120536/2,sun,1433.5e6,'Saturn')
uranus = Planet(86.6e24,51118/2,sun,2872.5e6,'Uranus')
neptune = Planet(102e24,2370/2,sun,4495.1e6,'Neptune')

''' ----- Simulation Configurations ----- '''

# Simulation #1: Binary System
names = ['Star 1', 'Star 2']
color = ['red','blue']
masses = np.array([5, 5])*sun.mass
xPositions = np.array([-2, 2])*AU
yPositions = np.array([0, 0])*AU
xVelocities = np.array([0, 0])*earth.orbitalVelocity
yVelocities = np.array([-1, 1])*earth.orbitalVelocity
sim1 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #2: Third Body Far From Binary System, Fast Initial Velocity
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([5, 5, 1])*sun.mass
xPositions = np.array([-2, 2, 0])*AU
yPositions = np.array([0, 0, 20])*AU
xVelocities = np.array([0, 0, -1])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim2 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #3: Third Body Far From Binary System, Slow Initial Velocity
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([5, 5, 1])*sun.mass
xPositions = np.array([-2, 2, 0])*AU
yPositions = np.array([0, 0, 20])*AU
xVelocities = np.array([0, 0, -0.75])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim3 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #4: Third Body Close To System, Fast Initial Velocity
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([5, 5, 1])*sun.mass
xPositions = np.array([10, 14, 12])*AU
yPositions = np.array([0, 0, 10])*AU
xVelocities = np.array([0, 0, -1.5])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim4 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #5: Third Body Close to System, Higher Mass
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([5, 5, 2])*sun.mass
xPositions = np.array([-2, 2, 0])*AU
yPositions = np.array([0, 0, 10])*AU
xVelocities = np.array([0, 0, -1])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim5 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]
        
# Simulation #6: Third Body Colinear with System, Equal Masses
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([5, 5, 5])*sun.mass
xPositions = np.array([-2, 2, 8])*AU
yPositions = np.array([0, 0, 0])*AU - 60*AU
xVelocities = np.array([0, 0, 0])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 1.5])*earth.orbitalVelocity
sim6 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #7: Three Bodies in an Equilateral Triangle, Third Has Higher Mass
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([2, 2, 2])*sun.mass
xPositions = np.array([1, -1, 0])*AU
yPositions = np.array([0, 0, 1])*AU
xVelocities = np.array([0, 0, 1])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim7 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #8: Three Bodies in an Equilateral Triangle, Third Has Higher Mass
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([1, 2, 2])*sun.mass*10
xPositions = np.array([1, -1, 0])*AU
yPositions = np.array([0, 0, 1])*AU
xVelocities = np.array([0, 0, 1])*earth.orbitalVelocity
yVelocities = np.array([-1, 1, 0])*earth.orbitalVelocity
sim8 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Simulation #9: Chris Moore’s Solution To the Three Body Problem
names = ['Star 1', 'Star 2', 'Star 3']
color = ['red','blue','green']
masses = np.array([1, 1, 1])*sun.mass
xPositions = np.array([-0.97000436, 0, 0.97000436])*AU
yPositions = np.array([0.24308753, 0, -0.024308753])*AU
xVelocities = np.array([0.4662036850, -0.93240737, 0.4662036850])*earth.orbitalVelocity
yVelocities = np.array([0.4323657300, -0.86473146, 0.4323657300])*earth.orbitalVelocity
sim9 = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

''' ----- Other system definitions ----- '''

# Our Solar System Information
names, masses, xPositions, xVelocities, yVelocities = ['The Sun'], [sun.mass], [0], [0], [0]
color = ['black','red','blue','green','orange','pink','purple','gray','yellow']
yPositions = np.zeros(len(color))
xVelocities = np.zeros(len(color))
for planet in sun.planets:
    names += [planet.name]
    masses += [planet.mass]
    xPositions += [planet.distance*1000]
    yVelocities += [planet.orbitalVelocity*1000]
ourSolarSystem = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]


# Moon, Earth, and Sun System Information
names = ['Sun', 'Earth', 'Moon']
color = ['red','blue','green']
masses = np.array([sun.mass, earth.mass, 7.348e22])
xPositions = np.array([0, AU, AU + 384400*1000])
yPositions = np.array([0, 0, 0])
xVelocities = np.array([0, 0, 0])
yVelocities = np.array([0, earth.orbitalVelocity, earth.orbitalVelocity + 3683*1000/3.6])
moonEarthSun = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]

# Many Bodies System Information
names = ['Star 1', 'Star 2', 'Star 3', 'Star 4', 'Star 5']
color = ['red','blue','green','orange','pink','purple','gray','yellow']
masses = np.array([1, 2, 2, 2, 4])*sun.mass
xPositions = np.array([-2, -1, 0, 0, 1])*AU/2
yPositions = np.array([0, 1, 1, -1, 1])*AU/2
xVelocities = np.array([1, 0, 1, 2, 0])*earth.orbitalVelocity
yVelocities = np.array([-3, 2, 2, 0, -2])*earth.orbitalVelocity
many = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]