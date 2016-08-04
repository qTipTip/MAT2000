from implicit_plot import implicit_plot
import mayavi.mlab as mlab
figw = mlab.figure(1, bgcolor=(0.1, 0.1, 0.1), size=(400, 400))
implicit_plot('z*y-x**2', (-2, 2, -2, 2, -2, 2), col_osurf=(0.87,0.086,0.086), col_isurf=(0.87,0.086,0.086), fig_handle=figw, opa_val=0.5, opaque=True, ori_axis=False)
implicit_plot('z-y**2', (-2, 2, -2, 2, -2, 2), col_osurf=(0.2, 0.2, 0.8), col_isurf=(0.2, 0.2, 0.8), fig_handle=figw, opa_val=0.5, opaque=True, ori_axis=False)
mlab.show()
