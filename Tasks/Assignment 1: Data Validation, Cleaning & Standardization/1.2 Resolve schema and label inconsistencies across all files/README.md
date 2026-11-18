# 1.2 Resolve schema and label inconsistencies across all files


## Description

- [x] Month labels are inconsistent within the monthly files: Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec. Standardize to a single convention and add a true date column in YYYY-MM-01 form for time series work

- Neighborhood vocabularies do not match across files. The monthly counts use East Village, City Center, Columbia, Marina, Cortez, Gaslamp, Core, and Outside Perimeter. The block grid uses South East Village, Golden Hill, Barrio Logan, and Sherman Heights. BlockMap_Coverage uses East Village South.
- [ ] Build a single crosswalk mapping every source label to one canonical neighborhood name, preserving the sub-area hierarchy
- [ ] Save crosswalk as CSV: "Neighborhood_Crosswalk.csv"
    ```
        @property
        def neighborhood_crosswalk(self) -> Path:
            return self.clean_data_dir / "Neighborhood_Crosswalk.csv"
    ```



- [x] BlockLevel_Counts.csv count_date values are wrapped in literal double quotes and currently parse as strings. Convert to ISO dates.
- [x] tents_structures in BlockLevel_Counts.csv is stored as float and contains one null. Decide and document the intended type and null handling.


- [x] Save cleaned versions of all delivered files with a _clean suffix
- [ ] Upload to Google Drive