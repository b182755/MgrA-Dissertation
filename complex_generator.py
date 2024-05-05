import subprocess

def combine_pdbqt_to_pdb(receptor_pdbqt_file, ligand_pdbqt_file, output_pdb_file):
    # Convert receptor PDBQT to PDB format
    subprocess.run(["obabel", receptor_pdbqt_file, "-O", "receptor.pdb"])

    # Convert ligand PDBQT to PDB format
    subprocess.run(["obabel", ligand_pdbqt_file, "-O", "ligand.pdb"])

    # Combine receptor and ligand PDB files into a single PDB file
    with open(output_pdb_file, "w") as outfile:
        subprocess.run(["cat", "receptor.pdb", "ligand.pdb"], stdout=outfile)

    # Clean up intermediate PDB files
    subprocess.run(["rm", "receptor.pdb", "ligand.pdb"])

# Example usage
receptor_pdbqt_file = "2bv6.pdb"
ligand_pdbqt_file = "molecule_13402992_out.pdb"
output_pdb_file = "2bv6_13402992_complex.pdb"

combine_pdbqt_to_pdb(receptor_pdbqt_file, ligand_pdbqt_file, output_pdb_file)
