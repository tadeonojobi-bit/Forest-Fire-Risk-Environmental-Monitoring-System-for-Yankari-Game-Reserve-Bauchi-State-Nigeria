import csv

# with open("ClimateData.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# # print("Number of Rows:", len(rows))
# # print("Columns:", list(rows[0].keys()))

# values = [] #inspecting the data to see what values are empty
# for row in rows:
# #     value = float(row['T2M']) #converting the string to a float
# #     values.append(value)

# # print("Largest Value:", max(values))
# # print("Smallest Value:", min(values))
# # print("count:", len(values))
#     raw = row['T2M'].strip() #removes empty values from the list in the table
#     if raw == "":
#         continue
#     values.append(float(raw)) #converting the string to a float
# print("Largest Value:", max(values))
# print("Smallest Value:", min(values))
# print("count:", len(values))

def inspect_column(filename, column): #converting all we did before to a function
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip() # using column is specifically because of the function, we want to be able to use any column in the table
        if raw == "":
            continue
        values.append(float(raw))
#return because we want to use the values in other parts of the code, not just print them
    return{ 
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
    } 

result = inspect_column("ClimateData.csv", "T2M")
print(result)
result = inspect_column("ClimateData.csv", "RH2M")
print(result)