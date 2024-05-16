import requests
from bs4 import BeautifulSoup
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from sklearn.metrics import pairwise_distances
import numpy as np
from urllib.request import urlopen
from urllib.parse import quote
#All the required imports for all the functions, just like in the code

from hempy.molecule_properties import *




# Test for function fetch_chemical_properties_by_cas(), it requires an already known CAS number
#imports : requests, BeautifulSoup, pandas
cas_number = '1972-08-3'  # CAS for THC
properties_data, chemical_url = fetch_chemical_properties_by_cas(cas_number)
display(properties_data)  # This will display the styled table in Jupyter Notebook or similar
print(f"URL to chemical page: {chemical_url}")



#Test for smiles_code(), with acetic acid
#imports: urlopen, quote
print(smiles_code("Acetic Acid"))



# Test for calculate_molecular_similarity(), with THC and CBD SMILES code which can be obtained with smiles_code()
#imports: Chem, AllChem, DataStructs, pairwise_distances
THC_smiles = "CCCCCC1=CC(=C2C3C=C(CCC3C(OC2=C1)(C)C)C)O"
CBD_smiles = "CCCCCC1=CC(=C(C(=C1)O)C2C=C(CCC2C(=C)C)C)O"

THC_mol = Chem.MolFromSmiles(THC_smiles)
CBD_mol = Chem.MolFromSmiles(CBD_smiles)

similarity_jaccard, similarity_tanimoto = calculate_molecular_similarity(THC_mol, CBD_mol)
print("Similarity (Jaccard):", similarity_jaccard)
print("Similarity (Tanimoto):", similarity_tanimoto)







