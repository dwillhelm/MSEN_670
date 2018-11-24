#!/bin/env/usr python

from pymatgen.io.vasp.inputs import *
import pymatgen as mg


cell = mg.Structure.from_file('POSCAR')
a = np.array([cell.lattice.abc]) 

def norm_shear(abc=None,strain=None):
    a = abc
    x = strain
    y = 1/(1-x**2) 
    shear = np.array([[1,x,0],[x,1,0],[0,0,y]])  
    out = np.dot(a,lat)
    
    return out


def tet_shear(abc=None,strain=None):
    a = abc
    x = strain
    y = 1/(1-x**2) 
    shear = np.array([[1,x,0],[x,1,0],[0,0,y]])  
    out = np.dot(a,lat)
    
    return out




