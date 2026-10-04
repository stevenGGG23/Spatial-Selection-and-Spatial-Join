Steven Gobran - E1: Spatial Selection and Spatial Join (QGIS)

FILES
1. Steven_Gobran_E1_selection.zip
   Crime points that fall within ZIP code 37072.
   Contains: .shp, .shx, .dbf, .prj, .cpg
   Result: 289 crime points

2. Steven_Gobran_E1_join.zip
   Davidson County ZIP codes with the number of crimes in each.
   Contains: .shp, .shx, .dbf, .prj, .cpg
   Result: 38 ZIP codes, crime count stored in the NUMPOINTS field

DATA
- Davidson.shp: Davidson County polygons with ZIP code field ZCTA5CE20
  (field identified from Davidson.xml: "2020 Census 5-digit ZIP Code Tabulation Area code")
- CrimeLocations.shp: crime point locations, last 3 years
- Both layers use EPSG:4326 (WGS 84)

TASK 1: SPATIAL SELECTION
1. Loaded Davidson and CrimeLocations into QGIS.
2. Select Features by Expression on Davidson: "ZCTA5CE20" = '37072'
   (344 Davidson polygons selected).
3. Vector > Research Tools > Select by Location:
   - Select features from: CrimeLocations
   - Geometric predicate: are within
   - Comparing to: Davidson (selected features only)
4. Exported the 289 selected points as Steven_Gobran_E1_selection (ESRI Shapefile).

TASK 2: SPATIAL JOIN
1. The Davidson layer is made of 13,379 small Census polygons, each tagged
   with a ZIP code. To count crimes per ZIP code, the polygons were first
   merged with Vector > Geoprocessing Tools > Dissolve on field ZCTA5CE20,
   giving 38 ZIP code polygons.
2. Vector > Analysis Tools > Count Points in Polygon:
   - Polygons: Dissolved
   - Points: CrimeLocations
   - Count field: NUMPOINTS
3. Exported the result as Steven_Gobran_E1_join (ESRI Shapefile).

RESULTS (top 5 ZIP codes by crime count)
  37013  11,833
  37211  10,593
  37203   8,466
  37207   8,116
  37115   7,323

Check: ZIP 37072 has 289 crimes in Task 2, matching Task 1.

NOTE
The 38 ZIP code counts total 103,218 out of 108,287 crime points.
The other 5,069 points fall just outside the Davidson County polygons,
so they are not counted in any ZIP code.
