#!/bin/bash
source /opt/intel/oneapi/setvars.sh > /dev/null 2>&1
/bin/echo "##" $(whoami) is compiling AI numba-dppy essentials Module3--  Pair wise - 3 of 5 pair_wise_kernel.py
python lab/l2_distance.py --steps 5 --size 1024 --repeat 5 -d 2 --json result_gpu.json
