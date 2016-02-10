from implicit_plot import implicit_plot
import mayavi.mlab as mlab
figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
implicit_plot('x**20 + y**20 + z**20 - 100',
              (-2, 2, -2, 2, -2, 2), col_osurf=(0.87,0.086,0.086),
              fig_handle=figw, opa_val=1.0, opaque=True, ori_axis=False)
mlab.show()
