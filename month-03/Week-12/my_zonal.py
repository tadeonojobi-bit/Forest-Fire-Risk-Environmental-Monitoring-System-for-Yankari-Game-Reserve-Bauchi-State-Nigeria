import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

zones = gpd.read_file(r"C:\Users\tadeo\Downloads\GeoDev_Lab\GeoDev_Lab_Starter_Data\Data\Processed\Yankari GR UTM32.shp")

for name in ["ndvi", "ndmi", "ndwi"]:
    with rasterio.open(f"data/processed/{name}_20260217.tif") as src:
        zones = zones.to_crs(src.crs)
        means = []
        for geom in zones.geometry:
            cells, _ = mask(src, [geom], crop=True, filled=False)
            cells = np.ma.masked_invalid(cells)  # also ignore NaN cells
            means.append(float(cells.mean()))
    zones[f"mean_{name}"] = np.round(means, 3)

zones.drop(columns="geometry").to_csv("month-03/Week-12/zonal_results.csv", index=False)
print(zones[["mean_ndvi", "mean_ndmi", "mean_ndwi"]])