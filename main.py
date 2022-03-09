# Year Project

# TO RUN A SIMULATION GO TO LINE 94
# Line 91: Set scale of turtle (default is 10/AU for larger systems)
# Line 92: Set number of timesteps for the simulation
# Line 93: Set timestep (in seconds)
# Line 94: >>> sys = run(NAME_OF_SYSTEM)
# system input is of type List
# Run script
# WARNING: Script cannot be paused or stopped without throwing an error.
#          Data will only be save if the simulation completes uninerrupted.

import time
import pickle
import numpy as np
from systemInfo import *
import matplotlib.pyplot as plt

def simulate(bodies):    
    for body in bodies:
        body.penup()                # Lift pen while location is determined
        body.hideturtle()           # Hide turtle, speeds up simulation
    
    timestep = tim                  # One day
    step = 1                        # Initial step
    while step <= numSteps:         # Run for a specified number of steps
        printProgress(step, bodies) # Print positions and velocities of bodies
        step += 1                   # Increase step by one
        force = {}
        for body in bodies:         # Sum all forces on body by other bodies in the system
            x_total_force = 0
            y_total_force = 0
            for otherBody in bodies:
                if body == otherBody:
                    continue                # Body does not exert a force on itself
                xForce, yForce = body.gravitationalForce(otherBody)
                x_total_force += xForce     # Add force of body to the sum of forces acting on the body
                y_total_force += yForce     # Add force of body to the sum of forces acting on the body
            force[body] = (x_total_force, y_total_force)

        # Update parameters of the body
        for body in bodies:
            xForce, yForce = force[body]
            
            # F = ma  --->  a = F/m  --->  v = F/m * s
            body.xVelocity += xForce / body.mass * timestep         # Update X velocity of the body
            body.yVelocity += yForce / body.mass * timestep         # Update Y velocity of the body

            # v = dx/t  ---> x = v * t
            body.xPosition += body.xVelocity * timestep             # Update X position of the body
            body.yPosition += body.yVelocity * timestep             # Update Y position of the body
            
            body.goto(body.xPosition*SCALE, body.yPosition*SCALE)   # Move turtle to body position
            body.dot(4)                                             # Mark position of the body with a dot
            
            # Record positions, velocities, and forces in each bodies history
            body.positions[0]  += [body.xPosition/1000]
            body.positions[1]  += [body.yPosition/1000]
            body.velocities[0] += [body.xVelocity/1000]
            body.velocities[1] += [body.yVelocity/1000]
            body.forces[0]     += [xForce]
            body.forces[1]     += [yForce]
            
def printProgress(step, bodies):
    print('Step #', str(step))
    for body in bodies:
        s = '{:12}  Pos (x,y): {:7.2E}km, {:10.2E}km    Vel (x,y): {:6.1f}km/s {:6.1f}km/s'.format(
            body.name, body.xPosition/1000, body.yPosition/1000, body.xVelocity/1000, body.yVelocity/1000)
        print(s)
    print()            
            
def run(systemInfo):
    # systemInfo = [names, color, masses, xPositions, yPositions, xVelocities, yVelocities]
    solarSystem = []
    for i in range(len(systemInfo[0])):
        body = Body()
        body.createRecords()
        body.name = systemInfo[0][i]
        body.mass = systemInfo[2][i]
        body.xPosition = systemInfo[3][i]
        body.yPosition = systemInfo[4][i]
        body.xVelocity = systemInfo[5][i]
        body.yVelocity = systemInfo[6][i]
        body.pencolor(systemInfo[1][i])
        solarSystem += [body]
    simulate(solarSystem)
    return solarSystem

SCALE = 100 / AU            # Scale: 20px = 1AU
turtle.setup(1000,750)      # Size of turtle window: 1000px wide, 750px tall
numSteps = 200              # Number of steps for simulation to run
tim = 24*3600*14            # Length of each timestep (seconds)
sys = run(sim9)

# Store data as an object
data = [ ['star x positions', 'star y positions', 'star x velocities', 'star y velocities', 'star x forces', 'star y forces'] ]
for body in sys:
    data += [ [body.positions[0], body.positions[1],
               body.velocities[0], body.velocities[1],
               body.forces[0], body.forces[1]] ]

# Saves a data set as a .obj file for future use
def saveFile(data, fileName):
    store_location = open(fileName+'.obj','wb')
    pickle.dump(data, store_location)
    store_location.close()
    
# Opens a .obj file containing a data set
def openFile(fileName):
    store_location = open(fileName+'.obj')
    data = pickle.load(store_location)
    store_location.close()
    return data
    
saveFile(data, 'results')       # Save data as 'results.obj'

''' Plot positions on same figure '''
t = np.array(np.linspace(0,numSteps,numSteps))*tim/3600/24/365.24      # Plot x axis in Days
color = iter(['red','blue','green','orange','pink','purple','gray','yellow'])

# Create Subplot
f, positions = plt.subplots(2, sharex=True)

# Plot X, Y Positions
for body in sys:
    c = next(color)
    positions[0].plot(t, body.positions[0], c = c, label=body.name)      # Star  X Position 
    positions[1].plot(t, body.positions[1], c = c, label=body.name)      # Star  Y Position

# Set Subplot Titles, Axis Labels, Legends
positions[0].set_title('X Position of Star vs. Timestep')
positions[1].set_title('Y Position of Star vs. Timestep')
positions[1].set(xlabel='Timestep (Years)')
positions[0].set(ylabel = 'X Position (km)')
positions[1].set(ylabel = 'Y Position (km)')
positions[0].legend(loc = 'best')
positions[1].legend(loc = 'best')
plt.figure(1)


''' Plot velocities on same figure '''
# Create Subplot
f, velocities = plt.subplots(2, sharex=True)
color = iter(['red','blue','green','orange','pink','purple','gray','yellow'])

# Plot X, Y Velocities
for body in sys:
    c = next(color)
    velocities[0].plot(t, body.velocities[0], c = c, label=body.name)        # Star  X Velocity
    velocities[1].plot(t, body.velocities[1], c = c, label=body.name)        # Star  Y Velocity

# Set Subplot Titles, Axis Labels, Legends
velocities[0].set_title('X Velocity of Star vs. Timestep')
velocities[1].set_title('Y Velocity of Star vs. Timestep')
velocities[1].set(xlabel='Timestep (Years)')
velocities[0].set(ylabel = 'X Velocity (km/s)')
velocities[1].set(ylabel = 'Y Velocity (km/s)')
velocities[0].legend(loc = 'best')
velocities[1].legend(loc = 'best')
plt.figure(2)