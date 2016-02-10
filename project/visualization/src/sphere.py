import mayavi.mlab as mlab
import numpy as np

from implicit_plot import implicit_plot

figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
implicit_plot('x**2 + y**2 + z**2 - {R:f}**2'.format(R=1), (-3, 3, -3, 3, -3, 3), fig_handle=figw, Nx=64, Ny=64, Nz=64, col_isurf=(0.0,0.2,0.8), opaque=True, ori_axis=False)
mlab.show()
