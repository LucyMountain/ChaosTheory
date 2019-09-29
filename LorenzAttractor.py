# Evolution of the Lorenz attractor
#
# The equations we are solving are
# dx = a (y - x)
# dy = x (r - z) - y
# dz = xy - bz
#
# Art Mountain 2019

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

nPoints = 10000

# Definition of parameters
a = 10
r = 28
b = 8 / 3
timestep = 0.01

# Starting values
x = 1
y = 1
z = 1

# lists to store x, y and z points
t, xdata, ydata, zdata = [], [], [], []
for j in range(nPoints):
    # Store current values
    t.append(j * timestep)
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)

    # Calculate new values
    x += timestep * a * (y - x)
    y += timestep * (x * (r - z) - y)
    z += timestep * (x * y - b * z)


# initialization function for phase space
def initPhaseSpace():
    # creating an empty plot/frame
    line.set_data([], [])
    line.set_3d_properties([])
    return line,


# animation function for phase space
def animatePhaseSpace(i):
    line.set_data(xdata[:i], ydata[:i])
    line.set_3d_properties(zdata[:i])
    return line,


# Create the plot, hiding the axes colouring so we see the line better
plt.style.use('dark_background')
fig = plt.figure()
plt.title('Lorenz attractor')
plt.axis('on')
ax = p3.Axes3D(fig)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)

# Set the axes to be the min to the max of each variable so we fit the plot on the screen
ax.set_xlim3d([min(xdata), max(xdata)])
ax.set_xlabel('X')
ax.set_ylim3d([min(ydata), max(ydata)])
ax.set_ylabel('Y')
ax.set_zlim3d([min(zdata), max(zdata)])
ax.set_zlabel('Z')

# call the animator
anim = animation.FuncAnimation(fig, animatePhaseSpace, init_func=initPhaseSpace,
                               frames=nPoints, interval=10, blit=True, repeat=False)
line, = ax.plot([], [], lw=2)
plt.show()

# Uncomment to save the animation as mp4 video file
# anim.save('LorenzAttractor.html',writer='imagemagick')
