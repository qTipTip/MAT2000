import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid


matplotlib.pyplot.xkcd()

delta = 0.025
xrange = arange(-5, 5.0, delta)
yrange = arange(-2.5, 2.5, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
# F = X**2 * (Y**2 - 1 - X)
F = X**2*(1 - Y**2 - X*Y**3)
G = 0

matplotlib.pyplot.axis('on')
matplotlib.pyplot.grid('on')
matplotlib.pyplot.contour(X, Y, (F - G), [0])

matplotlib.pyplot.savefig('case_1.pdf')

