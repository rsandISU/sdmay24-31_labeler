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
            file_path = input("File path doesn't exist. Re-enter lidar data path (CSV format):\n")
            
        while(file_path[len(file_path)-3:len(file_path)].lower() != "csv"):
            print(file_path[len(file_path)-3:len(file_path)])
            file_path = input("Incorrect file type. Re-enter lidar data path (CSV format):\n")

        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_data.append([row['X'], row['Y'], row['Z'], row['Reflectivity']])
    print("Success")

extra_data_from_csv()