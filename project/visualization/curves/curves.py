import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid


matplotlib.pyplot.xkcd()

delta = 0.025
xrange = arange(-2.5, 5.0, delta)
yrange = arange(-2.5, 2.5, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
F = Y**2
G = X**2 + X**3 

matplotlib.pyplot.axis('off')
matplotlib.pyplot.contour(X, Y, (F - G), [0])

matplotlib.pyplot.savefig('double_point.pdf')

