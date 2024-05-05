# Read the top 1,000 Unidock scores and file names
unidock_file = "top_10k_unidock_scores.txt"
unidock_data = {}

with open(unidock_file, "r") as file:
    for line in file:
        filename, score = line.strip().split(": ")
        molecule_id = filename.split('_')[1].split('.')[0]
        unidock_data[molecule_id] = float(score)

# Read the top 1,000 AutoDock scores and file names
autodock_file = "autodock_top_10k_bindingenergy_results.txt"
autodock_data = {}

with open(autodock_file, "r") as file:
    next(file)  # Skip the header line
    for line in file:
        parts = line.strip().split("\t")
        filename = parts[0]
        score = float(parts[1])
        molecule_id = filename.split('_')[1].split('.')[0]
        autodock_data[molecule_id] = score

# Find the common molecules between Unidock and AutoDock
common_molecules = set(unidock_data.keys()) & set(autodock_data.keys())

# Print the number of common molecules and the list of common molecules
print(f"Number of common molecules: {len(common_molecules)}")
print("Common Molecule IDs:")
for molecule_id in common_molecules:
    print(molecule_id)




