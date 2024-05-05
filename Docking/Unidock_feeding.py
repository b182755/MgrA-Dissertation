import os
import subprocess

# Define function to run UniDock for a batch of ligands
def run_unidock_batch(batch, input_repo_name, repo_index):
    repo_name = f"{input_repo_name}_UnidockResults_{repo_index}"
    output_dir = os.path.join(base_output_dir, repo_name)

    # Define UniDock command and execute it
    command = ['unidock',
               '--receptor', receptor_path,
               '--gpu_batch'] + batch + \
              ['--search_mode', 'fast',
               '--scoring', 'vina',
               '--center_x', str(center_x),
               '--center_y', str(center_y),
               '--center_z', str(center_z),
               '--size_x', str(size_x),
               '--size_y', str(size_y),
               '--size_z', str(size_z),
               '--num_modes', '1',
               '--dir', output_dir]

    try:
        subprocess.run(['nohup'] + command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, repo_name  # Indicate success and return the repository processed
    except subprocess.CalledProcessError as e:
        error_message = f"Error running UniDock for batch {batch} in repository {repo_name}: {e}"
        print(error_message)
        return False, repo_name  # Indicate failure and return the repository processed

# Define parameters
receptor_path = "/home/s2021783/2bv6.pdbqt"
base_output_dir = "/home/s2021783/MgrA/UnidockResumeResults"
center_x = 79.939
center_y = 3.114
center_z = 5.221
size_x = 30.0
size_y = 30.0
size_z = 30.0

# Define path to the file containing ligand file paths
ligands_file_path = "half_repos_ligand_files.txt"  # Adjust the path accordingly

# Read ligand file paths from the file
with open(ligands_file_path, "r") as file:
    ligand_file_paths = [line.strip() for line in file if line.strip()]  # Remove any leading/trailing whitespace and ignore empty lines

# Define batch size
batch_size = 10000
files_per_repo = 1000000

# Open log file for writing
with open("ligand_processing_log.txt", "w") as log_file:
    repo_index = 1
    processed_files = 0
    input_repo_name = os.path.basename(os.path.splitext(ligands_file_path)[0])

    # Process ligands in batches
    for i in range(0, len(ligand_file_paths), batch_size):
        batch = ligand_file_paths[i:i + batch_size]  # Extract current batch

        # Run UniDock for the batch
        success, processed_repo = run_unidock_batch(batch, input_repo_name, repo_index)

        # If there's an error processing a batch, print it to the console
        if not success:
            print(f"Error processing batch {batch} in repository {processed_repo}")

        processed_files += len(batch)

        # Check if it's time to create a new repository
        if processed_files >= files_per_repo:
            repo_index += 1
            processed_files = 0

print("All ligands processed.")






