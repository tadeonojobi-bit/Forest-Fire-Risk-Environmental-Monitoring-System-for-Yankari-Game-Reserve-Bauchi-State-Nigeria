import geopandas as gpd
import numpy as np
import rasterio
import matplotlib.pyplot as plt

index = "ndvi"
title = "NDVI, Yankari Game Reserve (Landsat 9, 17 Feb 2026)"
cmap = "RdYlGn"
vmin, vmax = 0.0, 0.45
out_png = "month-03/Week-12/my_map_ndvi.png"

zones = gpd.read_file("C:/Users/tadeo/Downloads/GeoDev_Lab/GeoDev_Lab_Starter_Data/Data/Processed/Yankari GR UTM32.shp")

with rasterio.open(f"data/processed/{index}_20260217.tif") as src:
    data = np.ma.masked_equal(src.read(1), -9999)  
    b = src.bounds
    zones = zones.to_crs(src.crs)

fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax, extent=(b.left, b.right, b.bottom, b.top))
zones.boundary.plot(ax=ax, color="black", linewidth=1)
fig.colorbar(im, ax=ax, label=index.upper(), shrink=0.7)
ax.set_title(title)
ax.set_xlabel("Easting (m)")
ax.set_ylabel("Northing (m)")
plt.savefig("month-03/Week-12/my_map_ndvi.png", dpi=200, bbox_inches="tight")
print("Saved:", out_png)