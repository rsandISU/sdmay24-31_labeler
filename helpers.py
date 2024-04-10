import math
import numpy as np
from tqdm import tqdm
import os.path
import csv

def extract_data_from_csv():
    """
    This function requests the lidar data in CSV format and returns a tuple containing the relevant lidar data (x, y, z, reflec).
    """
    raw_data = [[],[],[],[]]
    
    file_path = input("Enter lidar data path (CSV):\n")

    while(not os.path.isfile(file_path)):
        file_path = input("File path doesn't exist. Re-enter lidar data path (CSV format):\n")
        
    while(file_path[len(file_path)-3:len(file_path)].lower() != "csv"):
        print(file_path[len(file_path)-3:len(file_path)])
        file_path = input("Incorrect file type. Re-enter lidar data path (CSV format):\n")

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            raw_data[0].append(float(row['X']))
            raw_data[1].append(float(row['Y']))
            raw_data[2].append(float(row['Z']))
            raw_data[3].append(float(row['Reflectivity']))
                
    print("Successfully extracted lidar data from csv")
    return raw_data

def voxelize_and_normalize_scan_with_intensity(scan, num_voxels_per_dimension):
    """
    This function takes in a scan and returns a voxelized and normalized scan.
    Note that this function differs from voxelize_and_normalize_scan in that it also utilizes the intensity values of the points.
    The resulting voxelized scan will be a 4D array instead of a 3D array.
    However, you can think of it as a 3D array, where each voxel simply has two properties:
        the number of points in the voxel and the average intensity value of the points in the voxel.

    :param scan: a list of... a list of x values, a list of y values, a list of z values, and a list of intensity values
    :param num_voxels_per_dimension: the number of voxels per dimension to divide the scans into
                                        (i.e. 32 means 32x32x32 voxels)
    :return: the voxelized scan, which is a 3D array of the number of points in each voxel
    """
    x_vals = scan[0]
    y_vals = scan[1]
    z_vals = scan[2]
    intensity_vals = scan[3]
    min_x = min(x_vals)
    max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)
    min_z = min(z_vals)
    max_z = max(z_vals)
    min_intensity = min(intensity_vals)
    max_intensity = max(intensity_vals)

    voxel_dict = {}

    for i in range(len(x_vals)):
        this_x = x_vals[i]
        this_y = y_vals[i]
        this_z = z_vals[i]
        this_intensity = intensity_vals[i]

        # find the voxel that this point belongs to
        x_voxel = int((this_x - min_x) / (max_x - min_x) * (num_voxels_per_dimension - 1))
        y_voxel = int((this_y - min_y) / (max_y - min_y) * (num_voxels_per_dimension - 1))
        z_voxel = int((this_z - min_z) / (max_z - min_z) * (num_voxels_per_dimension - 1))
        if voxel_dict.get((x_voxel, y_voxel, z_voxel)) is None:
            voxel_dict[(x_voxel, y_voxel, z_voxel)] = [(this_intensity - min_intensity) / (max_intensity - min_intensity)]
        else:
            voxel_dict[(x_voxel, y_voxel, z_voxel)].append((this_intensity - min_intensity) / (max_intensity - min_intensity))

    max_density = 0
    min_density = math.inf
    for key in voxel_dict.keys():
        density = len(voxel_dict[key])
        if density > max_density:
            max_density = density
        if density < min_density:
            min_density = density

    voxelized_scan = np.zeros((num_voxels_per_dimension, num_voxels_per_dimension, num_voxels_per_dimension, 2))

    for key in voxel_dict.keys():
        # each voxel will contain an ordered pair of the density of points in that voxel and the average intensity of those points
        voxelized_scan[key[0]][key[1]][key[2]][:] = np.array(float(len(voxel_dict[key]) - min_density) / (max_density - min_density), np.mean(voxel_dict[key])) #TODO: make sure this really works

    print("Successfully voxelized data")

    return voxelized_scan