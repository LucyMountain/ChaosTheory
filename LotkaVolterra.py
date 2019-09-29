# Evolution of the Lotka-Volterra equations
#
# Art Mountain 2019

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# What type of plot to show
showPhaseSpace = 1
nPoints = 1000

# Definition of parameters
# The equations we are solving are
# dx = a x - b xy
# dy = -cx + d xy
a = 1
b = 1
c = 2
d = 1
timestep = 0.01
ee = -0.001

# Starting values
nRabbits = c / d + 1
nFoxes = a / b + 1

# lists to store x and y axis points 
t, xdata, ydata = [], [], []
for j in range(nPoints):
    # Store current values
    t.append(j * timestep)
    xdata.append(nRabbits)
    ydata.append(nFoxes)

    # Calculate new values
    oldNumRabbits = nRabbits
    nRabbits += nRabbits * timestep * (a - b * nFoxes) + ee * nRabbits * nRabbits * timestep
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
plt.style.use('dark_background')
plt.axis('on')
tMax = max(t)
xMax = max(xdata)
yMax = max(ydata)

# call the animator - there are 2 possible plots - time series and phase space
if showPhaseSpace:
    plt.title('Lotka-Volterra phase space')
    ax = plt.axes(xlim=(0, xMax * 1.25), ylim=(0, yMax * 1.25))
    anim = animation.FuncAnimation(fig, animatePhaseSpace, init_func=initPhaseSpace,
                                   frames=nPoints, interval=10, blit=True, repeat=False)
else:
    plt.title('Lotka-Volterra time series')
    ax = plt.axes(xlim=(0, tMax), ylim=(0, max(xMax, yMax) * 1.25))
    anim = animation.FuncAnimation(fig, animateTimeSeries, init_func=initTimeSeries,
                                   frames=nPoints, interval=10, blit=True, repeat=False)

line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
plt.show()
# Uncomment to save the animation as mp4 video file 
# anim.save('LotkaVolterra.html',writer='imagemagick')
