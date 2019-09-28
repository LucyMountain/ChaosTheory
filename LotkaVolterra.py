import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
import numpy as np 
plt.style.use('dark_background')

# What type of plot to show
showPhaseSpace = 0
nPoints = 1000

# Definition of parameters
a = 20
b = 3
c = 30
d = 1
timestep = 0.002

# Starting values
nRabbits = 20
nFoxes = 5

# lists to store x and y axis points 
t, xdata, ydata = [], [], []
for i in range(nPoints):
    # Store current values
    t.append(i * timestep)
    xdata.append(nRabbits)
    ydata.append(nFoxes)

    # Calculate new values
    oldNumRabbits = nRabbits
    nRabbits += nRabbits * timestep * (a - b * nFoxes)
    nFoxes += nFoxes * timestep * (-c + d * oldNumRabbits)

# initialization function for time series
def initTimeSeries(): 
    # creating an empty plot/frame 
    line.set_data([], [])
    line2.set_data([], [])
    return line, 

# animation function for time series
def animateTimeSeries(i): 
    line.set_data(t[:i], xdata[:i])
    line2.set_data(t[:i], ydata[:i])
    return line, line2,

# initialization function for phase space
def initPhaseSpace(): 
    # creating an empty plot/frame 
    line.set_data([], [])
    return line, 

# animation function for phase space
def animatePhaseSpace(i): 
    line.set_data(xdata[:i], ydata[:i])
    return line, 

# Plot setup - set the axes to be 1.25x the largest value so we fit the plot
fig = plt.figure()
tMax = max(t)
xMax = max(xdata)
yMax = max(ydata)
	
# displaying the axis details 
plt.axis('on') 

# call the animator - there are 3 possible plots
if showPhaseSpace:
    plt.title('Lotka-Volterra phase space')
    ax = plt.axes(xlim=(0, xMax * 1.25), ylim=(0, yMax * 1.25))
    anim = animation.FuncAnimation(fig, animatePhaseSpace, init_func=initPhaseSpace,
                                   frames=nPoints, interval=10, blit=True)
else:
    plt.title('Lotka-Volterra time series')
    ax = plt.axes(xlim=(0, tMax), ylim=(0, max(xMax, yMax) * 1.25)) 
    anim = animation.FuncAnimation(fig, animateTimeSeries, init_func=initTimeSeries, 
                                   frames=nPoints, interval=10, blit=True)    

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2) 
plt.show()
# Uncomment to save the animation as mp4 video file 
#anim.save('coil.html',writer='imagemagick') 
