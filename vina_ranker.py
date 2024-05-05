import os
import shutil
from tqdm import tqdm

# Define the directories containing the PDBQT files
pdbqt_directories = [
    "/home/s2021783/MgrA/UnidockResults",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_0",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_1",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_2",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_3",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_4",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_5",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_6",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_7",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_8",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_9",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_10",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_11",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_12",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_13",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_14",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_15",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_16",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_17",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_18",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_19",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_20",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_21",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_22",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_23",
    "/home/s2021783/MgrA/UnidockResumeResults/output_batch_24",
]

# Define the output directory for the top 1 million ligands
output_directory = "/home/s2021783/MgrA/Top1MillionLigands"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Initialize a dictionary to store ligand scores
ligand_scores = {}

# Initialize tqdm progress bar
with tqdm(total=len(pdbqt_directories), desc="Processing Directories") as pbar_dir:
    # Iterate through all directories
    for pdbqt_directory in pdbqt_directories:
        # Get the total number of PDBQT files for tqdm progress bar
        total_files = sum(1 for _ in os.listdir(pdbqt_directory) if _.endswith(".pdbqt"))

        # Initialize tqdm progress bar for current directory
        with tqdm(total=total_files, desc=f"Processing Files in {pdbqt_directory}") as pbar_file:
            # Iterate through all PDBQT files in the directory
            for filename in os.listdir(pdbqt_directory):
                if filename.endswith(".pdbqt"):
                    with open(os.path.join(pdbqt_directory, filename), "r") as file:
                        # Read the file line by line
                        for line in file:
                            # Check for the line containing autovina score
                            if line.startswith("REMARK VINA RESULT:"):
                                # Split the line based on whitespace
                                parts = line.split()
                                # Extract the autovina score (the fourth value)
                                if len(parts) >= 4:
                                    autovina_score = float(parts[3])
                                    # Store the autovina score in the dictionary
                                    ligand_scores[filename] = autovina_score
                                    break  # Exit the loop after finding the score in the file
                    # Update tqdm progress bar for files
                    pbar_file.update(1)
        # Update tqdm progress bar for directories
        pbar_dir.update(1)

# Sort the ligand scores in ascending order
sorted_scores = sorted(ligand_scores.items(), key=lambda x: x[1], reverse=False)

# Define a file to log errors
error_log_file = "error_log.txt"

# Copy the top 1 million ligands to the output directory
print("Copying Top 10,000 Ligands to Output Directory...")
with open(error_log_file, "w") as error_file:
    for ligand_name, _ in tqdm(sorted_scores[:10000], desc="Copying Files"):
        copied = False
        for pdbqt_directory in pdbqt_directories:
            try:
                src_file_path = os.path.join(str(pdbqt_directory), str(ligand_name))
                shutil.copy2(str(src_file_path), os.path.join(str(output_directory), str(ligand_name)))
                copied = True
                break
            except FileNotFoundError:
                continue
            except Exception as e:
                error_file.write(f"Error copying {ligand_name} from {pdbqt_directory}: {e}\n")
                break
        if not copied:
            pass
