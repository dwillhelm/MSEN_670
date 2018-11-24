
import pymatgen as mg
from pymatgen.electronic_structure.plotter import BSPlotter
from pymatgen.ext.matproj import MPRester

myapi = '9V30uOARCi8yFPKT'
que = MPRester(myapi) 

mpid = input('Enter MP-id=\n')

def brz_from_mpid(mpid):
    mpid = mpid
    bs = que.get_bandstructure_by_material_id(mpid)
    bzplot = BSPlotter(bs)
    bzplot.plot_brillouin().show()

brz_from_mpid(mpid) 

