from implicit_plot import implicit_plot
from birational_transform import birational_transform

import mayavi.mlab as mlab
figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
expr = '(x**2 + y**2 + z**2 + 2*y - 1) * ((x**2 + y**2 + z**2 -2*y - 1)**2 - 8*z**2) + 16*x*z*(x**2 + y**2 + z**2 - 2*y - 1) - 1.0'
for  i in range(2):
    implicit_plot(birational_transform(expr, iterations=i),
                  (-5, 5, -5, 5, -5, 5), col_osurf=(0.87,0.086,0.086), col_isurf=(1.00, 1.00, 1.00),
                  fig_handle=figw, opa_val=1.0, opaque=True, ori_axis=False, Nx=101, Ny=101, Nz=101)
    mlab.show()
