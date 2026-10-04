"""
Davidson County crime analysis: spatial selection and spatial join.

Reproduces the QGIS workflow in Python with GeoPandas.

Usage:
    pip install geopandas matplotlib
    python spatial_analysis.py
"""

from pathlib import Path

import geopandas as gpd

DATA = Path("data")
OUT = Path("output")
ZIP_FIELD = "ZCTA5CE20"   # from Davidson.xml: 2020 Census 5-digit ZIP Code Tabulation Area
TARGET_ZIP = "37072"

OUT.mkdir(exist_ok=True)

# Load layers (both are EPSG:4326)
davidson = gpd.read_file(DATA / "Davidson" / "Davidson.shp")
crimes = gpd.read_file(DATA / "CrimeLocation" / "CrimeLocations.shp")
print(f"Davidson polygons: {len(davidson):,}   Crime points: {len(crimes):,}")

# Task 1: spatial selection
# Same as QGIS: Select by Expression on ZIP, then Select by Location (are within)
zip_area = davidson[davidson[ZIP_FIELD] == TARGET_ZIP]
selection = gpd.sjoin(crimes, zip_area[["geometry"]], predicate="within")
selection = selection.drop(columns="index_right")
selection.to_file(OUT / "Steven_Gobran_E1_selection.shp")
print(f"Task 1: {len(selection):,} crimes within ZIP {TARGET_ZIP}")

# Task 2: spatial join (count points in polygon)
# The Davidson layer is many small Census polygons tagged with a ZIP code,
# so dissolve them into one polygon per ZIP first.
zips = davidson.dissolve(by=ZIP_FIELD).reset_index()[[ZIP_FIELD, "geometry"]]
counts = gpd.sjoin(crimes, zips, predicate="within").groupby(ZIP_FIELD).size()
zips["NUMPOINTS"] = zips[ZIP_FIELD].map(counts).fillna(0).astype(int)
zips.to_file(OUT / "Steven_Gobran_E1_join.shp")

print(f"Task 2: {len(zips)} ZIP codes, {zips.NUMPOINTS.sum():,} crimes counted")
print(zips.sort_values("NUMPOINTS", ascending=False)[[ZIP_FIELD, "NUMPOINTS"]].head().to_string(index=False))
