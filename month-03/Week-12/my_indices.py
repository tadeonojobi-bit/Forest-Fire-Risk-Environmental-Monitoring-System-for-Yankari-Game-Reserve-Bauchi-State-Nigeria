import numpy as np
import rasterio

folder = "C:/Users/tadeo/Downloads/GeoDev_Lab/GeoDev_Lab_Starter_Data/Data/Processed/"

def read_band(name):
    with rasterio.open(folder + name) as src:
        return src.read(1).astype("float32"), src.profile

green_raw, profile = read_band("L9_B3_CLP.tif")
red_raw, _ = read_band("L9_B4_CLP.tif")
nir_raw, _ = read_band("L9_B5_CLP.tif")
swir_raw, _ = read_band("L9_B6_CLP.tif")

valid = (green_raw > 0) & (red_raw > 0) & (nir_raw > 0) & (swir_raw > 0)

green = green_raw * 0.0000275 - 0.2
red = red_raw * 0.0000275 - 0.2
nir = nir_raw * 0.0000275 - 0.2
swir = swir_raw * 0.0000275 - 0.2

def norm_diff(a, b):
    out = np.full(a.shape, -9999, dtype="float32")
    total = a + b
    ok = valid & (total != 0)
    out[ok] = (a[ok] - b[ok]) / total[ok]
    return out, ok

indices = {
    "ndvi": norm_diff(nir, red),    # (NIR - Red) / (NIR + Red)
    "ndmi": norm_diff(nir, swir),   # (NIR - SWIR1) / (NIR + SWIR1)
    "ndwi": norm_diff(green, nir),  # (Green - NIR) / (Green + NIR)
}

profile.update(dtype="float32", nodata=-9999, count=1)
for name, (arr, ok) in indices.items():
    print(name.upper(), "range:", round(float(arr[ok].min()), 3), "to", round(float(arr[ok].max()), 3))
    print("Mean", name.upper() + ":", round(float(arr[ok].mean()), 3))
    with rasterio.open(f"data/processed/{name}_20260217.tif", "w", **profile) as dst:
        dst.write(arr, 1)
    print(f"Saved data/processed/{name}_20260217.tif")