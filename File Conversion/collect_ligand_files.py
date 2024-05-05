import os
import tqdm

# Define the parent directory containing subdirectories with PDBQT ligand files
ligands_parent_dir = "/home/s2021783/MgrA/Top1MillionInput"

# Initialize an empty list to store ligand file paths
ligand_files2 = []

# Count the total number of ligand files
total_files = sum(len(files) for _, _, files in os.walk(ligands_parent_dir))

# Initialize progress bar for ligand list creation
with tqdm.tqdm(total=total_files, desc="Collecting Ligand Files") as pbar:
    # Iterate over subdirectories in the parent directory
    for dirpath, _, filenames in os.walk(ligands_parent_dir):
        for filename in filenames:
            # Check if the file is a PDBQT ligand file
            if filename.endswith(".pdbqt"):
                # Construct the full path to the ligand file
                ligand_file_path = os.path.join(dirpath, filename)
                # Append the ligand file path to the list
                ligand_files2.append(ligand_file_path)
                # Update progress bar
                pbar.update(1)

# Save the list of ligand file paths to a file
with open("Top1MilLigands_files.txt", "w") as f:
    for ligand_file in ligand_files2:
        f.write(f"{ligand_file}\n")

print("List of ligand files saved to Top1MilLigands_files.txt.")
