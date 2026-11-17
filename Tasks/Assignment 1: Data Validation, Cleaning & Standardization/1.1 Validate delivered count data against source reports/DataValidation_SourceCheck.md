# DataValidation_SourceCheck


## Random sample 

The random sample contains 40 items. Each item was verified with the DSDP monthly PDF that can be finded at [this website](https://downtownsandiego.org/clean-and-safe/unhoused-care/).

The error rate is: 15.00%. This is the table that contains the rows that have some inconsistency. The colum "Status" represents the motif of its inconsistency. There are two files not finded at the website. One is wrong and the correct value is after the '-' (234, in the case). And there are three NaN at the csv.


| Índice | Area          | Month | Count | Year | Component  | Area Type    | Status                |
| ------ | ------------- | ----- | ----- | ---- | ---------- | ------------ | --------------------- |
| 0      | Marina        | Feb   | 62.0  | 2017 | total      | neighborhood | not_found_at_the_site |
| 1      | East Village  | Oct   | 649.0 | 2017 | total      | neighborhood | not_found_at_the_site |
| 34     | South East EV | Apr   | 43.0  | 2025 | total      | sub-area     | not_ok-234            |
| 35     | City Center   | Aug   | NaN   | 2025 | total      | neighborhood | not_ok-NaN            |
| 37     | Cortez        | July  | NaN   | 2025 | vehicle    | neighborhood | not_ok-NaN            |
| 39     | East Village  | Nov   | NaN   | 2025 | individual | neighborhood | not_ok-NaN            |



## Core

Findings

- The "Core" is a area without a sub-area
- It only apears at 2017, 2018 and 2019
 
Visualizing the "Core" area at the [december 2018 map](https://downtownsandiego.org/wp-content/uploads/2019/04/December-2018-Homeless-Count_FINAL.pdf) and comparing with the [december 2025 map](https://downtownsandiego.org/wp-content/uploads/2026/01/December-2025-Sleep-counts-W-maps.pdf), the "Core" is the same of "City Center"


