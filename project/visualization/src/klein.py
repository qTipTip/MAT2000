from implicit_plot import implicit_plot
import mayavi.mlab as mlab
figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
implicit_plot('(x**2 + y**2 + z**2 + 2*y - 1) * ((x**2 + y**2 + z**2 -2*y - 1)**2 - 8*z**2) + 16*x*z*(x**2 + y**2 + z**2 - 2*y - 1)',
              (-5, 5, -5, 5, -5, 5), col_osurf=(0.87,0.086,0.086), col_isurf=(1.00, 1.00, 1.00),
              fig_handle=figw, opa_val=1.0, opaque=True, ori_axis=False)
mlab.show()
