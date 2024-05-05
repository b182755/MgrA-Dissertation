import os
import shutil
from tqdm import tqdm

# Function to copy ligands from source repository to destination repository
def copy_ligands_to_combined_repo(src_repo_path, dest_repo_path):
    for file_name in os.listdir(src_repo_path):
        if file_name.endswith(".pdbqt"):
            src_file_path = os.path.join(src_repo_path, file_name)
            dest_file_path = os.path.join(dest_repo_path, file_name)
            shutil.copy(src_file_path, dest_file_path)

# Paths to your source repositories
repository_paths = [
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_1",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_2",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_3",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_4",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_5",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_6",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_7",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_8",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_9",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_10",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_11",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_12",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_13",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_14",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_15",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_16",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_17",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_18",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_19",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_20",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_21",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_22",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_23",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_24",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_25",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_26",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_27",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_28",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_29",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_30",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_31",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_32",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_33",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_34",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_35",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_36",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_37",
    "/home/s2021783/MgrA/LigandPDBQT/pdbqt_repository_38",
    # Add paths to other repositories here
]

# Path to the destination combined repository
combined_repo_path = "/home/s2021783/MgrA/LigandList"

# Create the combined repository if it doesn't exist
if not os.path.exists(combined_repo_path):
    os.makedirs(combined_repo_path)

# Total number of ligands copied
total_ligands_copied = 0

# Initialize tqdm progress bar
with tqdm(total=len(repository_paths), desc="Copying ligands") as pbar:
    # Copy ligands from each source repository to the combined repository
    for repo_path in repository_paths:
        copy_ligands_to_combined_repo(repo_path, combined_repo_path)
        # Update progress bar
        pbar.update(1)
        # Update total number of ligands copied
        total_ligands_copied += len(os.listdir(repo_path))

print(f"Combined ligands from {len(repository_paths)} repositories into {combined_repo_path}")
print(f"Total ligands copied: {total_ligands_copied}")



