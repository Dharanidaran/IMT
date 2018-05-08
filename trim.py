import os
import csv


cwd = os.getcwd()
filename = "OneStar.csv"

filepath = os.path.join(cwd,"data",filename)
# filename_to_write = "modelSampleKatC.csv"

fileobject =  open(filepath,encoding = 'utf-8',errors="ignore")
# writeobject = open(filename_to_write,'w')


csvReader = csv.reader(fileobject,delimiter =";")
# csvWriter = csv.writer(writeobject,delimiter=";")


stop_iter = 1
for row in csvReader:

	print(row[13],row[19].replace(";",""))
	if stop_iter == 10000:
		break
	stop_iter = stop_iter+1

	print(stop_iter)