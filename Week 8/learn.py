#def with_print(x):
#    print(x * 100)

#def with_return(x):
#    return(x * 100)

#a = with_print(5)
#b = with_return(5)

#print('a is', a)
#print('b is', b)

#print(b + 1)
#print(a + 1)

# with open('ClimateData.csv') as f: 
#     for lines in f.readlines()[1:]:
#         print(lines.strip().split(','))

import csv  # A module that allows us to read and write CSV files

with open('ClimateData.csv', encoding='utf-8-sig') as f: #This opens the csv and prevents numbers to be read as strings
    reader = csv.DictReader(f)
    for row in reader:
        print(row['DOY'], '->', row['T2M'], '->', row['RH2M'])