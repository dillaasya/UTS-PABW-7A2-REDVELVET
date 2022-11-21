import csv 
file = open("Cars.csv")

type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
        rows.append(row)
print(rows)