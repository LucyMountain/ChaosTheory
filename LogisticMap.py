# Evolution of the 1-d logistic map
#
# x -> k x (1-x)
#
# Art Mountain 2019

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Definition of parameters
nPoints = 100
kMin = 0
kMax = 4
k = 1.5

# Starting value
xInitOffset = 0.1

# lists to store values of t and x
t = np.linspace(0, nPoints, num=nPoints+1, endpoint=True)
xdata = np.zeros(nPoints)

def setUpData():
    global t, xdata, k
    # Start close to the fixed point
    x = max(0.3, min(0.9, 1 - 1/k - xInitOffset))
    for j in range(nPoints):
        # Store current values
        xdata[j] = x

        # Calculate new values
        x = k * x * (1 - x)


# initialization function for time series
def initLogisticMap():
    # creating an empty plot/frame 
    line.set_data([], [])
    return line,


# animation function for time series
def animateLogisticMap(i):
    line.set_data(t[:i], xdata[:i])
    return line,


# Calculate the data for the plot
setUpData()

# Plot setup - set the axes to be 1.25x the largest value so we fit the plot
plt.style.use('dark_background')
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
plt.axis('on')
tMax = max(t)
xMax = max(xdata)

plt.title('Logistic map evolution')

# Slider for k value
axcolor = 'lightgoldenrodyellow'
axSlider = plt.axes((0.15, 0.05, 0.65, 0.03), facecolor=axcolor)
kSlider = Slider(axSlider, 'k Value', kMin, kMax, valinit=k, valstep=(kMax - kMin) / 1000)


def update(val):
    global k
    k = kSlider.val
    setUpData()
    fig.canvas.draw_idle()


kSlider.on_changed(update)

# Call the animator
axes = plt.axes(xlim=(0, tMax), ylim=(0, max(1, xMax * 1.25)))
animatedPlot = animation.FuncAnimation(fig, animateLogisticMap, init_func=initLogisticMap,
                                       frames=nPoints, interval=10, blit=True, repeat=True)

line, = axes.plot([], [], lw=2)
plt.show()

# Uncomment to save the animation as mp4 video file
# animatedPlot.save('logisticMap.html',writer='imagemagick')
