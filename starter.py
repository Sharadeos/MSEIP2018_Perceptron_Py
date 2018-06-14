#Starter code to import the CSV file

import csv
with open('iris-binary-normalized.csv', newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
		
	for row in csvreader:
		slength = float(row[0])
		swidth = float(row[1])
		plength = float(row[2])
		pwidth = float(row[3])
		label = int(row[4])
		print(row)
			

			