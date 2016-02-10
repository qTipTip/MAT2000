from implicit_plot import implicit_plot
import mayavi.mlab as mlab

figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
phi = 1.618
phi_squared = 1.618**2

implicit_plot('4*(%f*x**2 - y**2)*(%f*y**2-z**2)*(%f*z**2-x**2) - (1 + 2*%f)*(x**2 + y**2 + z**2 - 1)**2' % (phi_squared, phi_squared, phi_squared, phi),
              (-2, 2, -2, 2, -2, 2), col_osurf=(1.0,0.086,1.0), col_isurf=(0.7, 0.1, 0.7),
              fig_handle=figw, opa_val=1.0, opaque=True, ori_axis=True)
mlab.show()
