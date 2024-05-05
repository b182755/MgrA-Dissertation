import os
import subprocess
from tqdm import tqdm

# Define the path to the parent directory containing ligand files
ligand_parent_dir = "/home/s2021783/MgrA/Top100kInput"

# List all ligand files in the parent directory
ligand_files = [os.path.join(ligand_parent_dir, filename) for filename in os.listdir(ligand_parent_dir) if filename.endswith('.pdbqt')]

# Define the path to the fld file
fld_file = "/home/s2021783/MgrA/AutoDock/PreProcessing/2bv6.maps.fld"

# Load the fld file before processing the ligands
load_fld_cmd = [
    "/home/s2263780/AutoDock-GPU/bin/autodock_gpu_128wi",
    "--ffile", fld_file,
    "--lfile", ligand_files[0],  # Use the first ligand file to load the .fld file
    "--nrun", "1"  # Only 1 run to load the .fld file
]

subprocess.run(load_fld_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Define the output directory
output_dir = "/home/s2021783/MgrA/AutoDock/AutodockResults/outputs"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Run AutoDock-GPU for each ligand
for ligand_file in tqdm(ligand_files, desc="Docking Progress", unit="ligands"):
    # Define the output file paths
    stdout_file = os.path.join(output_dir, f"{os.path.basename(ligand_file)}.stdout.txt")
    pdbqt_file = os.path.join(output_dir, f"{os.path.basename(ligand_file)}.pdbqt.1.pdbqt")

    cmd = [
        "/home/s2263780/AutoDock-GPU/bin/autodock_gpu_128wi",
        "--ffile", fld_file,
        "--lfile", ligand_file,
        "--nrun", "20",
        "--dlg2stdout", "1",  # Write dlg file output to stdout
        "--gbest", "1"  # Output single best pose as pdbqt file
    ]

    try:
        with open(stdout_file, "w") as stdout:
            subprocess.run(cmd, check=True, stdout=stdout, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"Error processing ligand {ligand_file}: {e}")















