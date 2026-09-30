# Yankari Fire-Risk Monitor

A GeoDev Lab project by Ade-Onojobi Taiwo — building, over one year, toward a coded, repeatable wildfire-risk monitoring system for Yankari Game Reserve, Nigeria.

## 1. Project Overview

This project is the coded, repeatable version of fire-risk analysis that, until now, has been done by hand, once, per study. It builds directly on earlier thesis work modeling fire risk at Ise Forest Reserve using Markov chain projection — the same underlying question, rebuilt here as a system that can be re-run rather than a one-off analysis. Over the course of the year, the project moves from basic GIS operations performed manually in QGIS toward an automated pipeline that pulls fresh data, recomputes risk, and outputs an updated map without manual re-analysis each time.

## 2. Main Research Question

**Which zones of Yankari Game Reserve show elevated wildfire risk during dry season, based on vegetation dryness, rainfall, terrain, and recent fire activity — and do the areas flagged as high-risk correspond to where fires have actually occurred?**

Each month's work answers a smaller piece of this question using one spatial operation at a time, building toward a combined risk score later in the year.

## 3. Study Area

**Yankari Game Reserve**, Bauchi State, Nigeria — approximately 2,244 km² of Sudan/Guinea savanna, centered near 9.75°N, 10.5°E. Yankari was chosen over other candidate sites (Ise Forest Reserve, Old Oyo National Park, Kamuku National Park) because annual dry-season bushfires — set mainly by poachers to flush game — are explicitly documented as one of the reserve's leading conservation threats, and its drier savanna climate gives far more usable, cloud-free satellite imagery during the fire season than a humid forest reserve would.

## 4. Datasets and Sources

| Dataset | Source | Format |
|---|---|---|
| Reserve boundary | [Protected Planet (WDPA)](https://www.protectedplanet.net) | Shapefile |
| Satellite imagery (Landsat 9, Collection 2 Level-2 Surface Reflectance, Bands 3/4/5/6) | [USGS EarthExplorer](https://earthexplorer.usgs.gov) | GeoTIFF |
| Elevation (SRTM 30m DEM) | [USGS EarthExplorer](https://earthexplorer.usgs.gov) / [OpenTopography](https://portal.opentopography.org) | GeoTIFF |
| Rainfall (CHIRPS Daily) | [Climate Hazards Center](https://data.chc.ucsb.edu/products/CHIRPS-2.0/) / [Early Warning Explorer](https://ewx3.chc.ucsb.edu/ewx/index.html) | GeoTIFF |
| Weather (temperature, 10m wind speed, relative humidity) | [NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/) | CSV |
| Fire detections (VIIRS S-NPP, 375m) | [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov) | Shapefile/CSV |

Full source links for each dataset, as downloaded, are listed in the Week 1 project brief (linked below).

## 5. Expected Output

A fire-risk map of Yankari Game Reserve combining vegetation dryness (NDVI/NDMI from Landsat), terrain (slope from the DEM), rainfall, and weather into a single risk score per zone — checked against real fire occurrence from FIRMS to see whether the model's high-risk areas match where fires actually burned. Later in the year, this moves from a single manually-produced map toward an automated pipeline that re-runs itself on a schedule.

## 6. Documentation and Weekly Deliverables

- [Week 1 — Project Brief](./week-1-project-brief/) — the research question and a source link for every dataset
- [Week 2 — Data Notes](./week-2-data-notes/) — what was downloaded and from where
- [Week 3 — Prepared Data & Quality Checks](./week-3-prepared-data/) — cleaned/reprojected data and the checks run on it
- [Week 4 — Analysis, Map & Summary](./week-4-analysis/) — the spatial operation, the output map, and `month-1-summary.md`

## 7. Key Findings — Month 1 Analysis

*Fill in with your actual result after running the spatial join:*

A spatial join (Join Attributes by Location, Summary: Count) between the FIRMS fire-detection points and the Yankari boundary — both reprojected to EPSG:32632 (UTM Zone 32N) — found **[X] fire detections** within the reserve boundary between December 2025 and February 2026, against an expectation of **[your pre-run estimate]**.

[One or two sentences on what this means for the main research question — e.g., whether fire activity was concentrated, sparse, near the boundary edges, etc. See `week-4-analysis/month-1-summary.md` for the full write-up.]
