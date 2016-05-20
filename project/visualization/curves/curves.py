import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid

from sys import argv


delta = 0.010
xrange = arange(-2, 2, delta)
yrange = arange(-2, 2, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
# F = X**2 * (Y**2 - 1 - X)
# F = X**2*(1 - Y**2 - X*Y**3)
# Example 1
# F = X*Y - X**6 - Y**6
F = X**2*(1 - Y**2 - X*Y**2)
G = 0

matplotlib.pyplot.axis('on')
matplotlib.pyplot.grid('off')
matplotlib.pyplot.contour(X, Y, (F-G), [0])
matplotlib.pyplot.axvline(x=0)
matplotlib.pyplot.xlabel('$y$')
matplotlib.pyplot.ylabel('$u$')

matplotlib.pyplot.savefig('node_affine_2.pdf')
