#!/usr/bin/env python

import pymatgen as mg
from pymatgen.io.vasp.inputs import * 
from pymatgen.ext.matproj import MPRester
import os,glob
import shutil as sh
import numpy as np

myapi = '9V30uOARCi8yFPKT'
q = MPRester(myapi) 


mplist = [134,1265,149] 

# download structures from MP: 
for i in mplist: 
    idd = 'mp-'+str(i)
    print(idd) 

    cell = q.get_structure_by_material_id(material_id=idd,
                                          final=True,
                                          conventional_unit_cell=True) 

    sd = [[True,True,True]]*cell.num_sites
    
    posid = '.'.join(cell.formula.split()).lower()

    Poscar(structure=cell, 
           selective_dynamics=sd,
           comment='MP POSCAR: {}'.format(cell.formula)
           ).write_file('POSCAR_{}'.format(posid))



poslist = glob.glob('POSCAR*')
for i in poslist: 
    cell = mg.Structure.from_file(i) 
    poscar = Poscar.from_file(i)
    incar = Incar.from_file('INCAR.relax') 
    kpoints = Kpoints 
    potcar = Potcar.from_file(
    










