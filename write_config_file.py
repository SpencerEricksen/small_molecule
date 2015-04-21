!/usr/bin/python

#usage: write.py crystal_lig.mol2 recpname ligname
#making new script to set up a vina configuration file

import csv 
import glob 
from rdkit import Chem 
from rdkit.Chem import AllChem 
from rdkit import Chem 
from rdkit.Chem import AllChem 
import sys

file_name = raw_input("file to be read")
xtal_molfile = sys.argv[1]
recp_name = sys.argv[2]
lig_name = sys.argv[3]

files = glob.glob('decoy*.csv')

#get receptor and ligand name for config file
receptor_name = raw_input("enter receptor name: ") 
ligand_name = raw_input("enter ligand name as name.mol2: ")

reading in file
m = Chem.rdmolfiles.MolFromMol2File( xtal_molfile, sanitize=False )

conf1 = m.GetConformer() 
centroid = Chem.rdMolTransforms.ComputeCentroid(conf1) 
x_center = centroid.x 
y_center = centroid.y 
z_center = centroid.z

atom_coord_x = [] 
atom_coord_y = [] 
atom_coord_z = [] 
for atom in m.GetAtoms(): 
    atom_index = atom.GetIdx() 
    pos = conf1.GetAtomPosition(atom_index) 
    atom_coord_x.append(pos.x) 
    atom_coord_y.append(pos.y) 
    atom_coord_z.append(pos.z)

#finding box dimensions:
padding = 5 
x_length = (max(atom_coord_x) + padding) - (min(atom_coord_x) - padding) 
y_length = (max(atom_coord_y) + padding) - (min(atom_coord_y) - padding) 
z_length = (max(atom_coord_z) + padding) - (min(atom_coord_z) - padding)

#writing out the config file
config_file = open("config_file_TEST.txt","w") 
config_file.write("receptor = str(receptor_name)\n") 
config_file.write("ligand = "+str(ligand_name)+"\n") 
config_file.write("center_x = "+str(x_center)+"\n") 
config_file.write("center_y = "+str(y_center)+"\n") 
config_file.write("center_z = "+str(z_center)+"\n") 
config_file.write("\n") 
config_file.write("size_x = "+str(x_length)+"\n") 
config_file.write("size_y = "+str(y_length)+"\n") 
config_file.write("size_z = "+str(z_length)+"\n") 
config_file.close()
