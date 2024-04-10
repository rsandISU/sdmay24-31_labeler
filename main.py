import numpy as np
from helpers import *

raw_data = extract_data_from_csv()

num_voxels_per_dimension = input("Enter the number of voxels per dimension you'd like (e.g. 10 means 10x10x10 voxels, if unsure, put 10):\n")

while(not num_voxels_per_dimension.isdigit() or int(num_voxels_per_dimension) <= 0):
    num_voxels_per_dimension = input("Invalid entry. Enter the number of voxels per dimension you'd like (e.g. 10 means 10x10x10 voxels, if unsure, put 10):\n")

voxelized_data = voxelize_and_normalize_scan_with_intensity(raw_data, int(num_voxels_per_dimension))