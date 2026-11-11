import geopandas as gpd

wards = gpd.read_file("Starterdata/processed/wards.gpkg", layers="wards")
wards.to_file("Starterdata/processed/week10_outputs.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv("month-03/week-10/wards_table.csv", index=False)
print(gpd.list_layers("Starterdata/processed/week10_outputs.gpkg"))