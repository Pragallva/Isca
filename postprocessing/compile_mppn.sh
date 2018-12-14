#!/usr/bin/env bash
# Compiles the mppncombine tool (tested on emps-gv2.ex.ac.uk) - copied from JP's compile.sh 


#-----------------------------------------------------------------------------------------------------
hostname=`hostname`
ppdir=./                 # path to directory containing the tool for combining distributed diagnostic output files
#-----------------------------------------------------------------------------------------------------



# 2. Load the necessary tools into the environment
#module purge
#module load netcdf-4.3.0-openmpi-intel
#imodule load netcdf/4.3
#module list


# 2. Load the necessary tools into the environment
module purge
source /project/tas1/pragallva/Fall_quarter_2017/Isca/src/extra/loadmodule
module list


netcdf_flags=`nf-config --fflags --flibs`
#--------------------------------------------------------------------------------------------------------
# compile combine tool
#cd $ppdir
cc -O -c `nc-config --cflags` mppnccombine.c
if [ $? != 0 ]; then
    echo "ERROR: could not compile combine tool"
    exit 1
fi
cc -O -o mppnccombine.x `nc-config --libs`  mppnccombine.o
if [ $? != 0 ]; then
    echo "ERROR: could not compile combine tool"
    exit 1
fi
#--------------------------------------------------------------------------------------------------------
