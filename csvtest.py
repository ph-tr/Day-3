import csv

# csvfile =  open ('csv1.csv')
with open('csv1.csv') as csvfile:
    spamreader  = csv.reader(csvfile)
    for row in spamreader:        
        print(', '.join(row))
# csvfile.close()