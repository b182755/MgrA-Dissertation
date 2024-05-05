import os
import re
from tqdm import tqdm

# Define directories containing the PDBQT files
unidock_directory = "/home/s2021783/MgrA/UnidockRun2Results/Top_1Mil_Out_0"

# Initialize dictionaries to store ligand scores
unidock_scores = {}

# Parse Unidock scores
print("Parsing Unidock scores...")
for filename in tqdm(os.listdir(unidock_directory), desc="Processing Unidock Files"):
    if filename.endswith(".pdbqt"):
        with open(os.path.join(unidock_directory, filename), "r") as file:
            for line in file:
                if line.startswith("REMARK VINA RESULT:"):
                    parts = line.split()
                    if len(parts) >= 4:
                        unidock_score = float(parts[3])
                        unidock_scores[filename] = unidock_score
                        break

# Sort the scores in ascending order
sorted_unidock_scores = sorted(unidock_scores.items(), key=lambda x: x[1])

# Store top 1,000 Unidock scores in a text file
with open("top_10k_unidock_scores.txt", "w") as file:
    for filename, score in sorted_unidock_scores[:10000]:
        file.write(f"{filename}: {score}\n")












