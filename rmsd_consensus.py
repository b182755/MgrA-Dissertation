#Gives RMSD and min. RMSD for two pdb or pdbqt files. Atoms have to be in the same order.
#Only works for pdb or pdbqt files - rmsd.ksh file1.pdb file2.pdb

function errhan {
print "USAGE: rmsd_min.ksh file1.pdbqt file2.pdbqt
Only works for pdb or pdbqt files that contain Autodock atom typing.
The first figure output is the minimum RMSD taking into account symmetry; atoms can be in any or>
The second figure output is the 'strict' RMSD; for this value to be correct the atoms must be in>
print $error
exit 1
}

if [[ ${#} == 0 ]]; then
  error="No input files detected"
  errhan
fi

if [[ $(grep -s "REMARK VINA RESULT:" $1) ]]; then
  print "Vina file format detected for $1;"
  print "Assuming you want to compare the first docking pose listed in the file ..."
  block1=$(egrep "^[AH][TE][OT][MA][ T][ M]|^MODEL|^ENDMDL" $1  | awk '/'MODEL\ 1'$/,/ENDMDL/' |>
else
  block1=$(grep  "^[AH][TE][OT][MA][ T][ M]" $1 )
fi
if [[ $(grep -s "REMARK VINA RESULT:" $2) ]]; then
  print "Vina file format detected for $2;"
  print "Assuming you want to compare the first docking pose listed in the file ..."
  block2=$(egrep "^[AH][TE][OT][MA][ T][ M]|^MODEL|^ENDMDL" $2  | awk '/'MODEL\ 1'$/,/ENDMDL/' |>
else
  block2=$(grep  "^[AH][TE][OT][MA][ T][ M]" $2 )
fi


types1=($(print "$block1" | cut -c78- ))
xcoords1=($(print "$block1" | cut -c31-38 ))
ycoords1=($(print "$block1" | cut -c39-46 ))
zcoords1=($(print "$block1" | cut -c47-54 ))