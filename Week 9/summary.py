import csv

def read_rows(filename):
    with open (filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    if len(values) == 0:
        return {"count": 0, "smallest": None, "Largest": None, "average": None}
    return {
        "count": len(values),
        "smallest": min(values),
        "Largest": max(values),
        "average": sum(values)/len(values)
     }

rows = read_rows("ClimateData.csv")
values = clean_values(rows, "T2M")
result = summarise (values)
print(result)

def summarize_all(filename, columns):
    rows = read_rows(filename)
    report = {}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarize_all("ClimateData.csv", ["T2M", "RH2M"])

for column, stats in report.items():
    print(column, "->", stats)