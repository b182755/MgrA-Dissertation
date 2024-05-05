import os
from tqdm import tqdm

# Directory containing the files
directory = '/home/s2021783/MgrA/AutoDock/AutodockResults/outputs'

# List of files in the directory
files = [f for f in os.listdir(directory) if f.endswith('.txt')]

# Dictionary to store the best binding energies and RMSD values
best_energies = {}

# Iterate over each file
for file_name in tqdm(files, desc="Processing files", ncols=100, mininterval=1.0):
    file_path = os.path.join(directory, file_name)

    # Read the file
    with open(file_path, 'r') as f:
        lines = f.readlines()

        # Find the line index where the data should start
        start_index = 0
        for i, line in enumerate(lines):
            if "RMSD TABLE" in line:
                start_index = i + 9  # Skip 8 lines and start reading from the 9th line
                break

        # Iterate over lines to extract data
        for line in lines[start_index:]:
            data = line.split()

            # Check if the line contains the expected number of columns
            if len(data) == 7:
                try:
                    rank, sub_rank, run, binding_energy, rmsd, cluster, reference = data
                    binding_energy = float(binding_energy)
                    rmsd = float(rmsd)

                    # Update best energy and RMSD for the file
                    if file_name not in best_energies or binding_energy < best_energies[file_name][0]:
                        best_energies[file_name] = (binding_energy, rmsd)

                except ValueError:
                    print(f"Skipping invalid line in file {file_name}: {line.strip()}")

# Sort energies based on binding energy in ascending order
sorted_energies = sorted(best_energies.items(), key=lambda x: x[1][0])

# Save top 1,000 results to a text file
output_file = '/home/s2021783/autodock_top_10k_bindingenergy_results.txt'
with open(output_file, 'w') as f:
    f.write("File Name\tBinding Energy\tRMSD\n")
    for file_name, (energy, rmsd) in sorted_energies[:10000]:
        f.write(f"{file_name}\t{energy}\t{rmsd}\n")

print(f"Top 10,000 results saved to {output_file}")
