with open('wards.csv') as f:
    lines = f.readlines()

# Print Each Line
# for line in lines:
    # print(line.strip())

# for line in lines[1:]:  # Skip the header line
#    parts = line.strip().split(',')
#    ward = parts[0]
#    area = parts[1]
#    print(ward, "has area ", area, "km²")

# for line in lines [1:]: #converting area from km² to hectares by adding the float() function to convert the area from string to float and multiplying by 100    
 #   parts = line.strip().split(',')
 #   wards = parts[0]
 #   area_km2 = float(parts[1])
  #  area_hectares = area_km2 * 100
  #  print(wards, "is", round(area_hectares, 1), "hectares")

for line in lines [1:]: #converting area from km² to hectares by adding the float() function to convert the area from string to float and multiplying by 100    
    parts = line.strip().split(',')
    wards = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:  # Check if the area is greater than 9 km²
        size = "large"
    else:
        size = "small"
    print(wards, "is", size)