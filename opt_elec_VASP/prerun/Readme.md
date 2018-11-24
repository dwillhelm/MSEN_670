# Readme

# An example of of running a relaxation followed by a band structure (and maybe optical) DFT calculation.  

Genearal Steps: 
1. Find/generate some POSCARs for bulk and 2D MoS2 using pymatgen, writing the manually, or using Vesta.  ( Make examples of all three)
2. Set up and run relaxation of 2D-MoS2 (INCAR.relax,KPOINTS.relax,POTCAR, run.vasp.relax). 
3. Set up electronic band structure calculation VASP files: 
              INCAR.scf
              INCAR.band
              KPOINTS.scf
              KPOINTS.band
              POSCAR
              POTCAR
              *(run.vasp.band)
4. Post-run analysis and plotting band structures
