## Protected Areas in Nigeria
- Source: https://www.protectedplanet.net/1332?site_pid=1332
- Downloaded: 12/09/2026
- 324 features, polygons
- Distinguishing Columns: WDPAID (1332.00), WDPA_PID (1332), PA_DEF (1), Name (Yankari), Orig_Name (Yankari), Desig (Game Reserve), Desig_Eng (Game Reserve), Desig_Type (National), IUCN_CAT (IV), INT_CRIT (Not Applicable), Marine (0), Rep_M_Area (0), GIS_M_AREA (2254.000), NO_TAKE (Not Applicable), STATUS (Designated), STATUS_YR (1991), GOV_TYPE (Sub-national ministry or agency), Own_Type (State)
- Geometry Type: Polygon
- No Nulls in Yankari Reserve
- Covers my LGA
- Extracted 12/09/2026
- Completeness: Data was complete
- Currency: Boundaries remain unchanged
- Positional: Dataset of study area seems to be a bit off from the basemap as at when recorded in 2010. This was flagged.
- Attribute: Labels are right
- Fitness: Data serves as the study area and can work for this project 

## Fire Records Data
- Source: https://firms.modaps.eosdis.nasa.gov/download/list.php
- Downloaded: 12/09/2026
- 2004 features, points (between Dec 1 2025 to Feb 28 2026)
- Distinguishing Columns: Latitude, Longitude, brightness, scan, track, acq_date, acq_time, satellite, instrument, confidence, version, bright_T31, FRP, Daynight, Type
- Geometry Type: Points
- No Nulls 
- Covers my Study Area
- Extracted 12/09/2026
- Completeness: Data was complete
- Currency: Current
- Positional: Dataset of points are within the study area.
- Attribute: Labels are right
- Fitness: Data serves as references and can work for this project

## Administrative Files
- Source: https://diva-gis.org/data.html
- Downloaded: 12/09/2026
- 775 features, polygons
- Distinguishing Columns: ID_0 (163), ISO (NGA), Name_0 (Nigeria),  ID_1 (5), Name_1 (Bauchi), ID_2 (91), Name_2 (Alkaleri), Type_2 (Local Authority), ENGTYPE_2 (Local Authority), NL_NAME_2 (NULL), VARNAME_2 (NULL)
- Geometry Type: Polygon
- Two Nulls in Yankari Reserve
- Covers my Study Area
- Extracted 12/09/2026
- Completeness: Data was incomoplete and contains a few nulls, hence, the fields cannot be used for computation
- Currency: Boundaries remain unchanged
- Positional: Dataset of study area seems to match with recent studies in terms of position.
- Attribute: Labels are right
- Fitness: Data serves as the study area and can work for this project

## Landsat Imageries (30m)
- Source: https://earthexplorer.usgs.gov/
- Downloaded: 12/09/2026
- Raster data LC9 L2 Bands 3, 4, 5, and 6, as well as Metadata
- Distinguishing Columns: unable to access attribute table
- Geometry Type: Nil
- Covers my Study Area
- Extracted 12/09/2026
- Completeness: Data was complete containing all bands required for computation
- Currency: Current for the area and corresponds to basemaps
- Positional: Dataset of study area seems to match with recent studies in terms of position.
- Attribute: Labels are right
- Fitness: Data serves as the study area and can work for this project

## Precipitation Imagery (GRIDMET 4km Daily)
- Source: https://app.climateengine.org/climateEngine
- Downloaded: 12/09/2026
- Raster data 
- Distinguishing Columns: unable to access attribute table
- Geometry Type: Nil
- Covers my Study Area
- Extracted 12/09/2026
- Completeness: Data was complete containing all bands required for computation
- Currency: Current for the area and corresponds to basemaps
- Positional: Dataset of study area seems to match with recent studies in terms of position.
- Attribute: Labels are right
- Fitness: Might be too large in terms of resolution, however, should suffice given the quality of data available worldwide for free


- CRS used: EPSG:32632 - WGS84 / UTM zone 32N which covers the study area and enables area measurements.
- All data sources were clipped
- Please see 5 quality checks within each dataset above
All files are located in C:\Users\tadeo\Downloads\GeoDev Lab\Data\Processed

[Precipitation Projected CLP.tif](https://github.com/user-attachments/files/32445866/Precipitation.Projected.CLP.tif)
[DEM CLP.tif](https://github.com/user-attachments/files/32445859/DEM.CLP.tif)
[L9_B6_CLP.tif](https://github.com/user-attachments/files/32445857/L9_B6_CLP.tif)
[L9_B3_CLP.tif](https://github.com/user-attachments/files/32445856/L9_B3_CLP.tif)
[Weather.zip](https://github.com/user-attachments/files/32445855/Weather.zip)
[L9_B4_CLP.tif](https://github.com/user-attachments/files/32445841/L9_B4_CLP.tif)
[L9_B5_CLP.tif](https://github.com/user-attachments/files/32445837/L9_B5_CLP.tif)
[Fire Records CLP.zip](https://github.com/user-attachments/files/32445836/Fire.Records.CLP.zip)


