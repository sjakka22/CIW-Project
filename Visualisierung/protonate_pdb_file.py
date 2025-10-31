#!/usr/bin/env python3

"""
Autor: Sujit Jakka
Input: PDB-Code eingegeben über das Terminal
Output: Protonierte Strukturen 
Protonierung erfolgt mit Protoss, nutze die REST-API
siehe https://proteins.plus/help/protoss_rest

Aufruf des Skripts erfolgt mit:
./protonate_pdb PDB-Code, e.g 
./protonate_pdb 1kzk

Output: protonated_protein_{}.pdb und protonated_ligand_{}.sdf
"""

import sys
import requests
import time
import subprocess
import os

protoss_url = "https://proteins.plus/api/protoss_rest"
if (len(sys.argv) != 2) or (type(sys.argv[1]) != str):
    sys.stderr.write('Usage: {} "PDB-Code, e. g. 1xdn"\n'.format(sys.argv[0]))
    exit(1)
pdb_code = sys.argv[1]
assert type(pdb_code) == str

job = {
    "protoss": {
        "pdbCode": pdb_code
    }
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(protoss_url, json=job, headers=headers)
data = response.json()

print("Job was created: ", data)
job_url = data.get("location")
if not job_url:
    raise Exception("Error in creating the job!")


while True:
    result = requests.get(job_url, headers=headers).json()
    print("Status:", result.get("message", result.get("status_code")))
    
    if result.get("status_code") == 200:
        print("Job abgeschlossen")
        print("Protein:", result["protein"])
        print("Ligands:", result["ligands"])
        print("Log:", result["log"])
        break
    elif result.get("status_code") == 202:
        print("Noch in Bearbeitung, warte 10 Sekunden ...")
        time.sleep(10)
    else:
        print("Fehler:", result)
        break

protein_url = result["protein"]
ligand_url = result["ligands"]
protein_pdb = requests.get(protein_url).text
ligand_sdf = requests.get(ligand_url).text

with open("protonated_protein_{}.pdb".format(pdb_code), "w") as p:
    p.write(protein_pdb)
p.close()

with open("protonated_ligand_{}.sdf".format(pdb_code), "w") as l:
    l.write(ligand_sdf)
l.close()

print("Dateien gespeichert: protonated_ligand_{}.sdf, protonated_protein_{}.pdb".format(pdb_code,pdb_code))

ligand_sdf_file = f"protonated_ligand_{pdb_code}.sdf"
ligand_pdb_file = f"protonated_ligand_{pdb_code}.pdb"

#  NEU: Konvertiere Ligand SDF -> PDB mit Open Babel
try:
    print("Konvertiere Ligand mit Open Babel ...")
    subprocess.run(
        ["obabel", ligand_sdf_file, "-O", ligand_pdb_file, "--gen3d"],
        check=True
    )
    print(f"Ligand erfolgreich konvertiert: {ligand_pdb_file}")
except FileNotFoundError:
    print("Fehler: Open Babel (obabel) ist nicht installiert oder nicht im PATH!")
except subprocess.CalledProcessError:
    print("Fehler bei der Konvertierung mit obabel!")

print("Fertig")
