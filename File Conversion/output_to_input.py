import os
import shutil
from tqdm import tqdm
from multiprocessing import Pool

# Define the parent directory containing the original ligand PDBQT files
parent_directory = "/home/s2021783/MgrA/LigandPDBQT"

# Define the directory containing the 1 million output PDBQT files
output_directory = "/home/s2021783/MgrA/Top100kLigands"

# Create a directory to store the extracted original ligand files
extracted_directory = "/home/s2021783/MgrA/Top100kInput"

# Create the extracted directory if it doesn't exist
if not os.path.exists(extracted_directory):
    os.makedirs(extracted_directory)

# Build a mapping of ligand IDs to their corresponding file paths
ligand_mapping = {}
for dirpath, dirnames, filenames in os.walk(parent_directory):
    for name in filenames:
        if name.endswith(".pdbqt"):
            ligand_id = name.split("_")[1].split(".")[0]  # Extract ligand ID from filename
            ligand_mapping[ligand_id] = os.path.join(dirpath, name)

def process_file(filename):
    if filename.endswith("_out.pdbqt"):
        # Extract the ligand ID from the output filename
        ligand_id = filename.split("_")[1].split(".")[0]

        # Check if the ligand ID exists in the mapping
        if ligand_id in ligand_mapping:
            original_filepath = ligand_mapping[ligand_id]
            shutil.copy2(original_filepath, os.path.join(extracted_directory, os.path.basename(original_filepath)))
            return

    print(f"Original ligand file not found for {filename}")

# Get list of output PDBQT files
output_files = [f for f in os.listdir(output_directory) if f.endswith("_out.pdbqt")]

# Use multiprocessing to process files in parallel with 31 threads
with Pool(31) as p:
    list(tqdm(p.imap(process_file, output_files), total=len(output_files), desc="Extracting Original Ligands"))

print("Extraction completed.")



