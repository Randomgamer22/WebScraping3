#Importing all the modules required
import csv
import pandas as pd

#Storing the file names in their own variables
file1 = 'bright_stars.csv'
file2 = 'brown_dwarfs.csv'

#Creating empty lists to append the data to
bright_stars_data = []
brown_dwarfs_data = []

#Opening the files using the read-key and appending the values to the blank lists
with open(file1,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        bright_stars_data.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        brown_dwarfs_data.append(i)

#Assigning the data after the first index to the star data lists
star_data_bright_stars = bright_stars_data[1:]
star_data_brown_dwarfs = brown_dwarfs_data[1:]

#Assigning the headers for the file
all_stars_headers = ['Name', 'Distance', 'Mass', 'Radius']

#Creating a blank list for combining the star_data form both the lists
all_stars_data =[]

#Appending the values in both the star_data lists to the final list
for i in star_data_bright_stars:
    all_stars_data.append(i)

for j in star_data_brown_dwarfs:
    all_stars_data.append(j)

#Writing the header and the final star data to the merged file
with open("all_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(all_stars_headers)   
    csvwriter.writerows(all_stars_data)
