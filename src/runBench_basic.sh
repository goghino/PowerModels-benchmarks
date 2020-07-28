#!/bin/bash

USERNAME=$(id -un)

#---------------------------
# prelude
#----------------------------
if [ $USERNAME == jkardos ]
then
    PREFIX="/users/jkardos/matpower_cpp"
    LIB_IPOPT="/users/jkardos/ipopt-schur/mybuild/lib"
    LIB_BLAS="/users/jkardos/lib:/opt/intel/compilers_and_libraries_2017.1.132/linux/mkl/lib/intel64_lin"
    LIB_PARDISO="/users/jkardos/lib"
    LIB_SCHUR="/users/jkardos/PowerGrid/lib"
    LIB_DEVSUITE=
fi

if [ $USERNAME == kardos ]
then
    PREFIX="/home/kardos/projects/matpower_cpp"
    LIB_IPOPT="/home/kardos/projects/ipopt-schur/myinstall/lib"
    LIB_BLAS="/apps/intel/16.0.3/mkl/lib/intel64"
    LIB_PARDISO="/home/kardos/Libraries/pardiso"
    LIB_SCHUR="/home/kardos/projects/PowerGrid/lib"
    LIB_DEVSUITE="/home/kardos/projects/devsuite"
    LIB_MPI="/apps/openmpi/3.1.2/lib"
fi

TARGET="$PREFIX/bin/matpowerCPP"


#---------------------------
# test case set up
#----------------------------
. config.sh

## specify tool for memory tracking
MEMORY_WRAPPER="/usr/bin/time -v"
TIMEOUT_WRAPPER="timeout --signal=KILL --verbose --foreground 5h"
MATLAB="/usr/global/bin/matlabR2018b"

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1

#---------------------------
# issue the jobs
#---------------------------
for OPFcase in "${grids[@]}"; do
for OPFsolver in "${solvers[@]}"; do
for OPFstart in "${OPFstarts[@]}"; do
for OPFvoltage in "${OPFvoltages[@]}"; do
for OPFbalance in "${OPFbalances[@]}"; do

sbatch <<-_EOF
#!/bin/bash
#SBATCH --job-name=SCOPF_${np}
#//SBATCH --reservation=HPC_tuesday
#//SBATCH --constraint=mc
#SBATCH --ntasks-per-node=${npernode}
#SBATCH --cpus-per-task=${nt}
#SBATCH --nodes=$((np/npernode+1))
#SBATCH --time=10:20:59
#SBATCH --output=job_${np}_${nt}_case${nbus}_ns${ns}.out
#SBATCH --error=job_${np}_${nt}_case${nbus}_ns${ns}.err
#SBATCH --mem=64148
#//SBATCH --partition=fat
#SBATCH --exclusive
#//SBATCH --partition=xphi

export LD_LIBRARY_PATH=$LIB_DEVSUITE:$LIB_SCHUR:$LIB_PARDISO:$LIB_IPOPT:$LIB_BLAS:$LIB_MPI:$LD_LIBRARY_PATH 
export OMP_NUM_THREADS=$nt
#export IPOPT_WRITE_MAT=1

printf "Case: "; echo $case
printf "$ns scenarios\n"
printf "Factorization $factorization \n"

# run the experiment
${MEMORY_WRAPPER} ${TIMEOUT_WRAPPER} /usr/global/bin/matlabR2018b -singleCompThread -nodisplay -nosplash -nodesktop -r "try benchmark_MATPOWER($Nperiod, $Nstorage, '$OPFcase',$OPFsolver, $OPFstart, $OPFvoltage, $OPFbalance); catch; end; quit" 2>&1 | tee data/$OPFcase-$OPFsolver-$OPFstart$OPFvoltage$OPFbalance.out
_EOF

done
done
done
done
done
