import rasterio

path = r"C:\Users\tadeo\Downloads\GeoDev_Lab\GeoDev_Lab_Starter_Data\Data\Processed\L9_B4_CLP.tif"  

with rasterio.open(path) as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print("Transform:")
    print(src.transform)

    # README check: width x resolution should equal right - left
    b = src.bounds
    print("width * res_x:", src.width * src.res[0])
    print("right - left:", b.right - b.left)
    print("Match:", abs(src.width * src.res[0] - (b.right - b.left)) < 1e-6)