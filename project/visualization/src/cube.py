from implicit_plot import implicit_plot
from birational_transform import birational_transform
import mayavi.mlab as mlab
figw = mlab.figure(1, bgcolor=(1, 1, 1), size=(400, 400))
expr = 'x**4 - y**2 - y**4'
for i in range(3):
    implicit_plot(birational_transform(expr, iterations=i),
                  (-1, 1, -1, 1, -1, 1), col_osurf=(0.87,0.086,0.086), col_isurf=(0.10,0.10,0.10),
                  fig_handle=figw, opa_val=0.5, opaque=True, ori_axis=False)

    mlab.show()
