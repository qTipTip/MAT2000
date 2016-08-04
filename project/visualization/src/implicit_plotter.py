import numpy as np
import mayavi.mlab as mlab

def implicit_plotter(expr, ext_grid, grid_res=(101, 101, 101),**kwargs):
    """
    Parameters
    ----------
    expr: string
        A string representation of 'f(x, y, z) - c = 0'
    ext_grid: 6-tuple
        The discrete grid '(xmin, xmax, ymin, ymax, zmin, zmax)'
    """
        
    # Create a new figure
    fig = mlab.figure(1, bgcolor=(1.0, 1.0, 1.0), fgcolor=(0, 0, 0), size=(800, 800))
    xl, xr, yl, yr, zl, zr = ext_grid
    Nx, Ny, Nz = grid_res
    x, y, z = np.mgrid[xl:xr:eval('{}j'.format(Nx)),
                       yl:yr:eval('{}j'.format(Ny)),
                       zl:zr:eval('{}j'.format(Nz))]

if __name__ == "__main__":
    implicit_plotter(expr='x - y**2', ext_grid=(0, 1, 0, 1, 0, 1))
