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
    # Add all directory paths here
]

# Define the output directory for the top 1000 ligands
output_directory = "/home/s2021783/MgrA/Top1000Ligands"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Assuming ligand_scores dictionary is already populated
ligand_scores = {
    # Populate ligand_scores with your ligand names and scores if it's not already populated
}

# Sort the ligand scores in ascending order
sorted_scores = sorted(ligand_scores.items(), key=lambda x: x[1], reverse=False)

# Print the top 3 ligands and their scores
print("Top 3 Ligands with Most Negative Scores:")
for i, (ligand_name, autovina_score) in enumerate(sorted_scores[:3], start=1):
    print(f"{i}. Ligand: {ligand_name}, Score: {autovina_score}")

# Copy the top 1000 ligands to the output directory
print("Copying Top 1000 Ligands to Output Directory...")
for ligand_name, _ in tqdm(sorted_scores[:1000], desc="Copying Files"):
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
            print(f"Error copying {ligand_name} from {pdbqt_directory}: {e}")
            break
    if not copied:
        print(f"Error: {ligand_name} not found in any directory.")
