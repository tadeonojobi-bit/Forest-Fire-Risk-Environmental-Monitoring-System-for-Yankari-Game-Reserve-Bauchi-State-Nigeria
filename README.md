# Forest Fire Risk and Environmental Monitoring System for Yankari Game Reserve, Bauchi State, Nigeria
## 1. Project Overview
This project aims to develop a geospatial system for assessing, monitoring, and visualizing forest fire risk within Yankari Game Reserve using Geographic Information Systems (GIS), remote sensing, environmental data, and geospatial programming. The system will integrate factors such as vegetation condition, land cover, temperature, rainfall, moisture, terrain, and historical fire occurrences to identify areas that may be more vulnerable to wildfire.

The project will begin as a relatively simple GIS-based fire-risk assessment using openly accessible geospatial datasets. Over the course of the GeoDev Lab programme, it will progressively evolve into a code-driven and repeatable geospatial application capable of automating data processing, generating fire-risk indicators, storing historical results, detecting changes over time, and presenting the information through an interactive web map or dashboard. This is the coded, repeatable version of fire-risk analysis that, until now, has been done by hand, once, per study. It builds directly on earlier thesis work modeling fire risk at Ise Forest Reserve using Markov chain projection — the same underlying question, rebuilt here as a system that can be re-run rather than a one-off analysis. Over the course of the year, the project moves from basic GIS operations performed manually in QGIS toward an automated pipeline that pulls fresh data, recomputes risk, and outputs an updated map without manual re-analysis each time.

The ultimate goal is not simply to produce a fire-risk map, but to build a reusable geospatial system that can continuously support environmental monitoring and wildfire management within Yankari Game Reserve.

## 2. Main Research Question

**Which zones of Yankari Game Reserve show elevated wildfire risk during dry season, based on vegetation dryness, rainfall, terrain, and recent fire activity — and do the areas flagged as high-risk correspond to where fires have actually occurred?**

Each month's work answers a smaller piece of this question using one spatial operation at a time, building toward a combined risk score later in the year.

## 3. Study Area

**Yankari Game Reserve**, Bauchi State, Nigeria — approximately 2,244 km² of Sudan/Guinea savanna, centered near 9.75°N, 10.5°E. Yankari was chosen over other candidate sites (Ise Forest Reserve, Old Oyo National Park, Kamuku National Park) because annual dry-season bushfires — set mainly by poachers to flush game — are explicitly documented as one of the reserve's leading conservation threats, and its drier savanna climate gives far more usable, cloud-free satellite imagery during the fire season than a humid forest reserve would.

## 4. Datasets and Sources
## Data Preparation Notes — Week 3
## What I prepared
- **Fire detections (FIRMS VIIRS S-NPP):** Downloaded in three monthly requests (Dec 2025, Jan 2026, Feb 2026) because of the 31-day limit, then combined with Merge Vector Layers into one shapefile that contained multiple point vectors. Clipped the points to the study area.
- **Reserve boundary (WDPA):** Yankari Game Reserve polygon, reprojected to EPSG:32632.
- **Elevation (SRTM 30m):** Clipped to the reserve extent and reprojected. Range: 145–1,368 m.
- **Landsat 9 (Level-2 Surface Reflectance):** Bands 3, 4, 5, 6 only. Already atmospherically corrected, so no extra correction was applied. 
- **Rainfall (CHIRPS daily):** Clipped to the Yankari extent. 
- **Weather (NASA POWER):** One CSV with temperature, 10 m wind speed and relative humidity. The metadata lines at the top were skipped on import, and it was loaded as a table with no geometry.

## Quality checks run
- **CRS:** Confirmed every spatial layer is in EPSG:32632 before any analysis.
- **Geometry validity:** Ran Check Validity on the boundary and fire points. Empty or invalid geometries: [none / number].
- **Row counts:** Merged FIRMS file has 2004 rows, equal to the sum of the three monthly files.
- **Date range:** All fire detections fall between 1 Dec 2025 and 28 Feb 2026.
- **Visual check:** Layers overlap correctly on the map, with a bit of an offset between the appearance of the study area on the imagery and on the shapefile data.

## Known limitations
- Landsat is a single date, while fire points cover three months.
- NASA POWER data is coarse (about 50 km grid), so it is effectively one value for the whole reserve.

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

# Month 1
## 6. Documentation and Weekly Deliverables

- [Week 1 — Project Brief](project-brief.md) — the research question and a source link for every dataset
- [Week 2 — Data Notes](DataNotes.md) — what was downloaded and from where
- [Week 3 — Prepared Data & Quality Checks](Data) — cleaned/reprojected data and the checks run on it
- [Week 4 — Analysis, Map & Summary](Month-1-summary.md) — the spatial operation, the output map, and `month-1-summary.md`

## 7. Key Findings — Month 1 Analysis

A spatial join (Join Attributes by Location, Summary: Count) between the FIRMS fire-detection points and the Yankari boundary — both reprojected to EPSG:32632 (UTM Zone 32N) — found **2004 records of fire occurrences** within the reserve boundary between December 2025 and February 2026, against an expectation of **3000+**. Further analysis is needed to be carried out to determine the fire risk score to be compared with the occurences of fire recorded by the satellite.

See [week-4-analysis/month-1-summary.md](Month-1-summary.md) for the full write-up.
See map results below

<img width="3507" height="2480" alt="Fire Records Map" src="https://github.com/user-attachments/assets/17fd6d76-1f82-40cc-bdba-127b59502656" />

# Month 2 — Development Environment and Early Python

Month 2 moves the project from point-and-click GIS towards code. The work covered setting up a Python development environment (Python 3.14, VS Code, the terminal and `uv`), managing a project with `uv`, and using Python to read, convert, classify and summarise tabular data. These are the building blocks for automating the Yankari fire-risk analysis in later months.

## Documentation and Weekly Deliverables

- [Week 5 — Development Environment Setup](Hello.py) — Python, VS Code and the terminal configured; `Hello.py` runs and prints `My setup works!`Encountered issues with installing uv. It was installed using pip install uv, however, this allows for difficulties in calling uv in different terminals like in VS code or windows powershell. The method used to fix this was a reinstallation using "winget install --id astral-sh.uv -e --source winget". Then, I waited for an installation, and I restarted the powershell terminal and checked the version for authentication using "uv --version"
- [Week 6 — Project Setup with uv](check.py) — project initialised with `uv`; `pandas` and `geopandas` added as dependencies; `check.py` prints the installed pandas version. Initiated the project using "uv init", then I observed the various sub packages formed within the environment. Pandas (a package used for enabling excel-type functions) was added using "uv add pandas" command. I experienced errors in using pandas as the main.py file did not exist after adding pandas. The initial code used was "uv run main.py". 
- [Week 7 — First Analysis Script](analyse.py) — `analyse.py` reads `Wards.csv`, converts each ward's area from km² to hectares and classifies each ward as large or small. 
- [Week 8 — Data Inspection](inspect_data.py) — `inspect_data.py` reports a CSV's row count and column names, and returns summary dictionaries (smallest, largest, count) for the area and population columns. `inspect_data.py` summarises the population and areas in the dummy data used as a result of a discovery in faulty csv dataset. A new dataset was obtained and run to achieve similar results.
- [Week 9 — Consolidation and Refactoring](Week09/summary.py) — `summary.py` reorganises the earlier steps into reusable functions (`read_rows`, `clean_values`, `summarise`) plus `summarize_all`, which summarises several columns in one run


## Technical Notes and Issues Resolved
**Week 5 — Running a script in PowerShell.** Typing `print("my setup works")` directly at the PowerShell prompt returned `Unable to initialize device PRN`, because PowerShell treated `print` as a Windows command, not Python. Running the saved script with `python hello.py` printed the expected output.

**Week 5 — Installing `uv`.** `uv` was first installed with `pip install uv`, but it could not be called reliably from other terminals such as the VS Code terminal and Windows PowerShell. It was reinstalled with `winget install --id astral-sh.uv -e --source winget`. Once the installation finished, PowerShell was restarted and the install was verified with `uv --version`.

**Week 6 — Project layout.** `uv init` created a packaged project, with code under `src/` and a `[project.scripts]` entry in `pyproject.toml`, so there is no root-level `main.py`. `uv run main.py` therefore failed. Scripts saved in the project folder, such as `check.py`, run directly with `uv run check.py`.

**Week 7 — Floating-point output.** Converting Mokola's area to hectares printed `930.0000000000001`, a normal floating-point rounding artefact. Values are rounded for display.

**Week 8 — Faulty source data.** The weather CSV (`Climate.csv`) was found to be faulty: it held a single day (20 Sep 2026) of missing `-999` values, and the temperature-range parameter instead of daily temperature. `inspect_data.py` was therefore tested on a placeholder dataset (`Placeholder.csv`: four wards with area and population) while a corrected download was obtained.

## Week 9 Results

The corrected weather data (`ClimateData.csv`, daily NASA POWER values) was summarised with `summarize_all`:

| Variable | Count | Smallest | Largest | Average |
|---|---|---|---|---|
| T2M — temperature at 2 m (°C) | 90 | 23.46 | 29.95 | 26.75 |
| RH2M — relative humidity at 2 m (%) | 90 | 12.44 | 37.18 | 23.20 |

A count of 90 matches the 90 days from 1 December 2025 to 28 February 2026, so the series covers the full dry-season window.

## Month 2 Reflection
Month 2 shifted the work from desktop GIS to scripts that can be re-run. The key lesson came in Weeks 8 and 9: summarising the data in code exposed that the weather data prepared in Month 1 was inaccurate, which led to a corrected download that now passes the same checks. The corrected dataset is ready to be combined with the other layers in the risk analysis.

## Month 3: geospatial Python and automation
Week 10: GeoPandas. Loaded, checked, joined and mapped my [layer name] in code.
