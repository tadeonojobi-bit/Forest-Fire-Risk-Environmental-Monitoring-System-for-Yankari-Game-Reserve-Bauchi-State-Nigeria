# Month 1 Summary

*Question:* How many FIRMS fire detections fell within Yankari Game Reserve's boundary within dry season (between Dec 2025 and Feb 2026)?

*Operation:* Spatial join (Join Attributes by Location, Summary: Count) in QGIS, both layers reprojected to EPSG:32632 (UTM Zone 32N) since that's the appropriate projected CRS for Bauchi State.

*Expected:* I expected over 3000 records based on visual estimates alone. 

*Got:* The count field contained a value of 2004 which corresponds to the number of records within the study area. The fact that I had filtered out for the Forest Reserve and clipped reduced the number of occurrences and made things easier.

*What surprised me:* For a forest reserve, there were more fire occurrences than I expected which were as a result of controlled fires and other anthropogenic factors.

*What data I still need:* I still need the NDVI/NDMI layer to combine with this into an actual risk score, not just a fire count
