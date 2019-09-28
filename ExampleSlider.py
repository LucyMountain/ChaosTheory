# Lotka-Volterra integrator
#
# Art Mountain 2019
#
import numpy as np
import pylab as p
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from scipy import integrate

a = 1.
b = 0.1
c = 1.5
d = 0.75
lambdaMin = 0.0
lambdaMax = 30.0
lambdaInit = 0.5
pLambda = lambdaInit
dLambda = 0.1
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.2)
t = np.arange(0.0, 1.0, 0.001)
mainPlotAxes = None

def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return np.array([ a*X[0] -   b*X[0]*X[1] ,
                     -c*X[1] + d*b*X[0]*X[1] ])

def drawChart(pLambda):
    # Use lambda
    a = pLambda * c
    
    # Integrate
    t = np.linspace(0, 15, 1000)              # time
    X0 = np.array([10, 5])                     # initials conditions: 10 rabbits and 5 foxes
    X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
    infodict['message']                     # >>> 'Integration successful.'

    # Display
    rabbits, foxes = X.T
    plt.cla()
    #if mainPlotAxes is not None:
    #    plt.axes = mainPlotAxes
    #ax = fig.gca()
    #legend = ax.legend()
    #legend.remove()
    plt.plot(t, rabbits, 'r-', label='Rabbits')
    plt.plot(t, foxes  , 'b-', label='Foxes')
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.title('Evolution of fox and rabbit populations')
    fig.canvas.draw_idle()
    mainPlotAxes = plt.axes
    
drawChart(lambdaInit)

# Lambda slider
axcolor = 'lightgoldenrodyellow'
axlambda = plt.axes([0.13, 0.025, 0.6, 0.04], facecolor=axcolor)
slambda = Slider(axlambda, 'Lambda', lambdaMin, lambdaMax, valinit=lambdaInit, valstep=dLambda)
def update(val):
    plambda = slambda.val
    drawChart(plambda)
slambda.on_changed(update)

# Switch control
switchax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(switchax, 'Switch', color=axcolor, hovercolor='0.475')
def reset(event):
    slambda.reset()
button.on_clicked(reset)

plt.show()
