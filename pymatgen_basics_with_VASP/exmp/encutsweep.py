#!/usr/bin/env python



import pymatgen as mg
from pymatgen.io.vasp.inputs import * 


# To sweep ENCUT values
encut_list = [] 


incar = Incar.from_file('INCAR_al')
poscar = Poscar.from_file('POSCAR.MP')
kpoints = Kpoints.from_file('KPOINTS_temp') 
potcar = Potcar.from_file('POTCAR_al')




