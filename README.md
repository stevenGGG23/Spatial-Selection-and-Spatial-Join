# Davidson County Crime Analysis: Spatial Selection & Spatial Join

Where are crimes concentrated in Nashville (Davidson County, TN)? This project uses QGIS and Python to answer two spatial questions with three years of reported crime locations:

1. **Spatial selection:** which crimes happened inside ZIP code 37072?
2. **Spatial join:** how many crimes happened in each ZIP code?

<img width="1512" height="804" alt="image" src="https://github.com/user-attachments/assets/7d1ef2af-8018-4b1e-802e-767d3cd0b806" />


## Key results

| | Result |
|---|---|
| Crime points analyzed | 108,287 |
| Crimes within ZIP 37072 (Task 1) | **289** |
| ZIP codes in Davidson County (Task 2) | **38** |
| Crimes counted inside a ZIP code | 103,218 |

**Top 5 ZIP codes by crime count**

| ZIP code | Crimes |
|---|---:|
| 37013 | 11,833 |
| 37211 | 10,593 |
| 37203 | 8,466 |
| 37207 | 8,116 |
| 37115 | 7,323 |

The full table is in [`crime_counts_by_zip.csv`](crime_counts_by_zip.csv). Crime is heaviest in downtown (37203) and the southeast (37013, 37211). The rural north and west have the fewest crimes.

## Data

| Layer | Type | Description |
|---|---|---|
| `Davidson.shp` | Polygons (13,379) | Davidson County Census polygons, each tagged with a ZIP code |
| `Davidson.xml` | Metadata | Column descriptions for the Davidson attribute table |
| `CrimeLocations.shp` | Points (108,287) | Locations of crimes reported in Davidson County over the last 3 years |

- **ZIP code field:** `ZCTA5CE20` (2020 Census 5-digit ZIP Code Tabulation Area, from `Davidson.xml`)
- **Coordinate system:** EPSG:4326 (WGS 84)
- Data was provided for a course assignment and is not included in this repo.

## Method

### Task 1: Spatial selection

1. **Select by Expression** on Davidson: `"ZCTA5CE20" = '37072'` (344 polygons)
2. **Select by Location** on CrimeLocations
   - Predicate: *are within*
   - Compared to: Davidson, *selected features only*
3. Export the selected points: `Steven_Gobran_E1_selection.shp`

**Result:** 289 crimes in ZIP 37072.

### Task 2: Spatial join

1. **Dissolve** Davidson on `ZCTA5CE20`. The layer is made of 13,379 small Census polygons, so they have to be merged into one polygon per ZIP code before counting. This step turns 13,379 polygons into 38.
2. **Count Points in Polygon**
   - Polygons: dissolved ZIP codes
   - Points: CrimeLocations
   - Output field: `NUMPOINTS`
3. Export the result: `Steven_Gobran_E1_join.shp`

**Check:** ZIP 37072 has 289 crimes in Task 2, which matches Task 1.

## Reproduce in Python

The same workflow is in [`spatial_analysis.py`](spatial_analysis.py), using GeoPandas.

```bash
pip install geopandas matplotlib
python spatial_analysis.py
```

Put the data in this layout first:

```
data/
├── Davidson/Davidson.shp (+ .shx .dbf .prj .cpg)
└── CrimeLocation/CrimeLocations.shp (+ .shx .dbf .prj .cpg)
```

Output:

```
Task 1: 289 crimes within ZIP 37072
Task 2: 38 ZIP codes, 103,218 crimes counted
```

## Repo structure

```
├── README.md
├── spatial_analysis.py        # GeoPandas version of the QGIS workflow
├── crime_counts_by_zip.csv    # Crime count for all 38 ZIP codes
├── images/
│   └── results_map.png        # Results map
└── output/                    # Exported shapefiles
    ├── Steven_Gobran_E1_selection.zip
    └── Steven_Gobran_E1_join.zip
```

## Notes

- 5,069 crime points (about 5%) fall just outside the Davidson County polygons, so they are not counted in any ZIP code. That's why the ZIP totals add up to 103,218 instead of 108,287.
- ZCTAs are Census approximations of USPS ZIP codes, so their boundaries can differ slightly from mailing ZIP codes.

## Tools

QGIS · Python · GeoPandas · Matplotlib

---

*Steven Gobran · Middle Tennessee State University*

<img width="1347" height="799" alt="image" src="https://github.com/user-attachments/assets/b1ae7f4a-6c4c-40d9-873b-1da3415088e6" />
<img width="1358" height="766" alt="image" src="https://github.com/user-attachments/assets/31bbce78-5a71-4e6d-8aa9-149eedd77d16" />


