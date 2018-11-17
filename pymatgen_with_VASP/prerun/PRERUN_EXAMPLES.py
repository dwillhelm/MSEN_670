#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pymatgen as mg
from pymatgen.io.vasp.inputs import *


# In[19]:


# convert the INCAR file into a python object
# typing 'incar' will show the Tags of the incar object
incar = Incar.from_file('INCAR')
print(incar)


# In[11]:


# An example of how to view a specific Tag
incar['ISIF']


# In[12]:


# Show the value of the ENCUT tag
incar['ENCUT']


# In[14]:


# Change ENCUT from 520 to 300
incar['ENCUT'] = 300
incar['ENCUT']


# In[18]:


# Notice the whole object is now updated
print(incar)


# In[89]:


# Example: Converting a POSCAR file to a pymatgen structure object...
cell = mg.Structure.from_file('POSCAR')
print(cell)


# In[20]:


# The structure object has a lot of information
print(cell.lattice)


# In[22]:


print(cell.lattice.a)


# In[46]:


print(cell.formula)
print(cell.atomic_numbers)
print(' ')
print(cell.cart_coords)
print(' ')
print(cell.volume)


# In[43]:


cell.lattice


# In[54]:


print(cell)


# In[94]:


new_lat = mg.Lattice.from_lengths_and_angles([1,1,1],[90,90,90])
print(new_lat)
print(' ')
cell.modify_lattice(new_lattice=new_lat)
print(cell)


# In[105]:


# We can use the pymatgen object to write a new POSCAR file
Poscar(structure=cell,comment='New POSCAR file').write_file('POSCAR_New')

# We can see the poscar in the pwd...
import os
os.listdir()


# In[96]:


# to convert a KPOINTS into a python object
kpoints = Kpoints.from_file('KPOINTS')
print(kpoints)


# In[99]:


# To change a kpts value
new_kpt = [5,5,5]
kpoints.kpts.clear()
kpoints.kpts.append(new_kpt)
print(kpoints)


# In[115]:


# With the INCAR, POSCAR, KPOINTS as python objects 
# it is easy to incorperate them into python scripts

# Example: 
incar = Incar.from_file('INCAR')
poscar = Poscar.from_file('POSCAR')
kpoints = Kpoints.from_file('KPOINTS')
potcar = Potcar.from_file('POTCAR')

# or ... 
vasp_set = VaspInput(incar=incar,
                     kpoints=kpoints,
                     potcar=potcar,
                     poscar=poscar)

# or ... (will only read from pwd and the files named INCAR, POSCAR, KPOINTS, POTCAR)
vasp_set = VaspInput.from_directory('.')
print(vasp_set)


# In[109]:


# import the 'os' and 'shutil' library
# os is an useful library for working in a Linux system
# It can be useful in creating subdirectories or moving files
import os
import shutil


# In[125]:


# Example - looping and stuff like that

for new_encut in [100,200,300]:
    vasp_set.write_input(output_dir=str(new_encut),make_dir_if_not_present=True)

os.listdir()


# In[149]:


# or ... 
cell = mg.Structure.from_file('POSCAR')
print(cell)


# In[150]:


cell.replace_species({'Li':'Cu'})
print(cell)
cell.species


# In[157]:


# another example ...

atomlist = ['Na','K','Rb','Cs']
for new_atom in atomlist: 
    cell = mg.Structure.from_file('POSCAR')
    cell.replace_species({'Li':new_atom})
    print(cell.species) 
    
    poscar = Poscar(cell)
    incar = Incar.from_file('INCAR')
    kpoints = Kpoints.from_file('KPOINTS')
    # IMPORTANT: you will need to compile the new POTCARs for the new structures
    # the potcar here would be wrong for all except Li2O
    # Use the get_potcar.sh script to get the correct POTCARs beforehand
    # for example, for Na2O use: get_potcar.sh Na O
    # and then rewrite it POTCAR_Na2O (before running loop)
    # and then potcar.from_file('POTCAR_Na2O') or to work in the loop 'POTCAR_'+new_atom
    potcar = Potcar.from_file('POTCAR')
    
    vasp_in = VaspInput(incar=incar,poscar=poscar,kpoints=kpoints,potcar=potcar)
    new_dir = 'run_'+new_atom
    vasp_in.write_input(output_dir=new_dir,make_dir_if_not_present=True)
    
       
    


# In[158]:


os.listdir() 


# In[ ]:




