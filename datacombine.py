import numpy as np
import pandas as pd
import sys,os
import pathlib,path

# listing file contents of a directory: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files

directory = "/Users/kristinafrazier/documents/projects/etsy/data/csv"
path = os.path.join(directory, "targetdirectory")

for path, subdirs, files in os.walk(directory):
    for name in files:
        print(pathlib.PurePath(path, name))

filenames = []

for path, subdirs, files in os.walk(directory):
    for name in files:
        filenames.append(pathlib.PurePath(path, name))

# would like to find a better way to filter only csv files
csv_files = filenames[1:-1]

# append all of the csv files into one file: https://stackoverflow.com/questions/2512386/how-to-merge-200-csv-files-in-python
combined_csv = pd.concat([pd.read_csv(f) for f in csv_files])

# export to a single CSV file
combined_csv.to_csv( "/Users/kristinafrazier/documents/projects/etsy/data/csv/all_etsy_listings_raw.csv", index=False )
