#!/bin/bash
#BATCH --job-name="npdes_test"
#SBATCH --output="npdes_test_o.%j.%N.out"
#SBATCH --error="npdes_test_e.%j.%N.out"
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gpus=4
#SBATCH --ntasks-per-node=4
#SBATCH --account=mia326
#SBATCH --export=ALL
#SBATCH -t 00:30:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sidsriva@gmail.com

### Deactivate the CPU stack
. /cm/shared/apps/spack/cpu/opt/spack/linux-centos8-zen2/gcc-10.2.0/anaconda3-2020.11-weucuj4yrdybcuqro5v3mvuq3po7rhjt/etc/profile.d/conda.sh
conda deactivate

### Reset to GPU stack and load the modules needed
module reset
module load anaconda3
module load openmpi/4.0.4-nocuda

### Activate the environment
. $ANACONDA3HOME/etc/profile.d/conda.sh
conda activate /expanse/projects/qstore/mia326/sids/pde
export LD_LIBRARY_PATH=/expanse/projects/qstore/mia326/sids/pde/lib:$LD_LIBRARY_PATH

### Set some MPI parameters
export OMPI_MCA_btl_openib_allow_ib=1
export OMPI_MCA_btl_openib_if_include="mlx5_0:1" 
export OMPI_MCA_btl=openib,self,vader

### Run using mpirun
mpirun -np 4 python main.py cnn-gpu4.ini
