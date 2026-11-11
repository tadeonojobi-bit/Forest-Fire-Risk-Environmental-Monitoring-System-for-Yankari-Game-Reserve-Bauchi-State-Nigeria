import geopandas as gpd

wards = gpd.read_file("Starterdata/processed/wards.gpkg", layer="wards")
first = wards.geometry.iloc[0]
print(type(first))
print(first)
print("valid:", first.is_valid)
print("centroid:", first.centroid)