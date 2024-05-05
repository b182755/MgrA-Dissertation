import os
import subprocess
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def get_pdbqt_files(input_dir):
    """Get a list of PDBQT files in the input directory."""
    return [filename for filename in os.listdir(input_dir) if filename.endswith(".pdbqt")]

def convert_pdbqt_to_sdf(input_dir, output_parent_dir, molecule_numbers):
    """Convert PDBQT files to SDF format for specified molecule numbers in a given input directory."""
    output_dir = os.path.join(output_parent_dir, "sdf_" + os.path.basename(input_dir))
    os.makedirs(output_dir, exist_ok=True)

    pdbqt_files = get_pdbqt_files(input_dir)

    progress_bar = tqdm(total=len(pdbqt_files), desc=f"Converting {input_dir}", unit="file", dynamic_ncols=True)

    for filename in pdbqt_files:
        molecule_number = filename.split("_", 1)[1].split(".")[0]  # Extract number from filename
        if molecule_number in molecule_numbers:
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, molecule_number + ".sdf")

            try:
                subprocess.run(["obabel", input_file, "-O", output_file], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(f"Error converting {input_file}: {e}")

        progress_bar.update(1)

    progress_bar.close()

if __name__ == "__main__":
    # Directory containing input directories
    parent_dir = "/home/s2021783/MgrA/LigandPDBQT"

    # Specify the location of the output parent directory
    output_parent_dir = "/home/s2021783/MgrA/LigandSDF"

    # File containing list of molecule numbers (just numbers)
    molecule_numbers_file = "/home/s2021783/top10kconsensus.txt"

    # Read molecule numbers from the file
    with open(molecule_numbers_file, 'r') as f:
        molecule_numbers = set(line.strip() for line in f)

    # Get a list of input directories
    input_dirs = [os.path.join(parent_dir, subdir) for subdir in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, subdir))]

    # Use 31 processes (maximum - 1 to avoid saturating all threads)
    num_processes = min(31, cpu_count() - 1)

    # Create a multiprocessing Pool with 31 processes
    with Pool(processes=num_processes) as pool:
        # Map the conversion function to each input directory
        pool.starmap(convert_pdbqt_to_sdf, [(input_dir, output_parent_dir, molecule_numbers) for input_dir in input_dirs])
