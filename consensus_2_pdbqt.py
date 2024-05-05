import os
import shutil

# Path to the file containing molecule identifiers
molecule_ids_file = "/home/s2021783/top10kconsensus.txt"

# Path to the directory containing the original input files
input_directory = "/home/s2021783/MgrA/Top100kInput"

# Path to the new directory where matched files will be saved
new_directory = "/home/s2021783/ConsensusTopInput"

# Read molecule identifiers from file
with open(molecule_ids_file, 'r') as file:
    # Create filenames from the identifiers by adding the necessary prefix and suffix
    expected_filenames = {f"molecule_{line.strip()}.pdbqt" for line in file}

# Ensure the new directory exists
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Copy files that match the molecule IDs to the new directory
for filename in os.listdir(input_directory):
    if filename in expected_filenames:
        # Define the source and destination file paths
        src = os.path.join(input_directory, filename)
        dst = os.path.join(new_directory, filename)
        # Copy the file
        shutil.copy(src, dst)
        print(f"Copied {filename} to {new_directory}")

print("File copying process complete.")
