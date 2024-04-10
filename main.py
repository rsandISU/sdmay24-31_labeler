import csv
import numpy as np
from helpers import *
import os.path

raw_data = []

def extra_data_from_csv():
    with open('test.csv', 'w', newline='') as newcsvfile:

        csvwriter = csv.writer(newcsvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        file_path = input("Enter lidar data path (CSV):\n")

        while(not os.path.isfile(file_path)):
            file_path = input("File path doesn't exist. Re-enter lidar data path (CSV):\n")

        if not os.path.isfile(file_path):
            print("File path doesn't exist")

        with open('2023-04-15_12-55-45.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_data.append([row['X'], row['Y'], row['Z'], row['Reflectivity']])
    print("Success")


# def extra_data_from_csv():
#     with open('test.csv', 'w', newline='') as newcsvfile:

#         csvwriter = csv.writer(newcsvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
#         file_path = input("Specify file path:\n")

#         with open('2023-04-15_12-55-45.csv', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 raw_data.append([row['X'], row['Y'], row['Z'], row['Reflectivity']])
#     print("Success")