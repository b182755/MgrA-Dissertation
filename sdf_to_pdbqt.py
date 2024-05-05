import os
import subprocess
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def get_subdirectories(parent_dir):
    """Get a list of subdirectories in the parent directory."""
    return [os.path.join(parent_dir, subdir) for subdir in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, subdir))]

def convert_sdf_to_pdbqt(input_dir, output_parent_dir):
    """Convert SDF files to PDBQT format in a given input directory."""
    output_dir = os.path.join(output_parent_dir, "pdbqt_" + os.path.basename(input_dir))
    os.makedirs(output_dir, exist_ok=True)

    sdf_files = [filename for filename in os.listdir(input_dir) if filename.endswith(".sdf")]

    progress_bar = tqdm(total=len(sdf_files), desc=f"Converting {input_dir}", unit="file", dynamic_ncols=True)

    for filename in sdf_files:
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".pdbqt")

        try:
            subprocess.run(["obabel", input_file, "-O", output_file], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file}: {e}")

        progress_bar.update(1)

    progress_bar.close()

if __name__ == "__main__":
    # Directory containing input directories
    parent_dir = "/home/s2021783/TheoDiss"

    # Specify the location of the output parent directory
    output_parent_dir = "/home/s2021783/MgrA/LigandPDBQT"

    # Get a list of input directories
    input_dirs = get_subdirectories(parent_dir)

    # Use 31 processes (maximum - 1 to avoid saturating all threads)
    num_processes = min(31, cpu_count() - 1)

    # Create a multiprocessing Pool with 31 processes
    with Pool(processes=num_processes) as pool:
        # Map the conversion function to each input directory
        pool.starmap(convert_sdf_to_pdbqt, [(input_dir, output_parent_dir) for input_dir in input_dirs])


