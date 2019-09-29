# Evolution of the 1-d logistic map
#
# x -> k x (1-x)
#
# Art Mountain 2019

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definition of parameters
nPoints = 100
k = 3.5

# Starting value
x = 0.25

# lists to store values of t and x
t, xdata = [], []
for i in range(nPoints):
    # Store current values
    t.append(i)
    xdata.append(x)

    # Calculate new values
    x = k * x * (1 - x)


# initialization function for time series
def initLogisticMap():
    # creating an empty plot/frame 
    line.set_data([], [])
    return line,


# animation function for time series
def animateLogisticMap(index):
    line.set_data(t[:index], xdata[:index])
    return line,


# Plot setup - set the axes to be 1.25x the largest value so we fit the plot
plt.style.use('dark_background')
fig = plt.figure()
tMax = max(t)
xMax = max(xdata)

# displaying the axis details 
plt.axis('on')

# call the animator - there are 3 possible plots
plt.title('Logistic map evolution')
ax = plt.axes(xlim=(0, tMax), ylim=(0, xMax * 1.25))
animatedPlot = animation.FuncAnimation(fig, animateLogisticMap, init_func=initLogisticMap,
                                       frames=nPoints, interval=10, blit=True, repeat=False)

line, = ax.plot([], [], lw=2)
plt.show()

# Uncomment to save the animation as mp4 video file
# animatedPlot.save('logisticMap.html',writer='imagemagick')
