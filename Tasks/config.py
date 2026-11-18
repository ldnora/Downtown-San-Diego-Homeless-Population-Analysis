"""
This file contains the unified configuration of paths used to save and load data.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Datasets:
    root_dir: Path = Path(__file__).resolve().parents[1]

    # DATA
    @property
    def data_dir(self) -> Path:
        return self.root_dir / "Data"

    # RAW
    @property
    def raw_data_dir(self) -> Path:
        return self.data_dir / "Raw"

    @property
    def raw_block_level_counts(self) -> Path:
        return self.raw_data_dir / "BlockLevel_Counts.csv"

    @property
    def raw_block_map_coverage(self) -> Path:
        return self.raw_data_dir / "BlockMap_Coverage.csv"

    @property
    def raw_downtown_block_grid(self) -> Path:
        return self.raw_data_dir / "Downtown_BlockGrid.csv"

    @property
    def raw_downtown_block_grid_geojson(self) -> Path:
        return self.raw_data_dir / "Downtown_BlockGrid.geojson"

    @property
    def raw_master_counts_adjusted(self) -> Path:
        return self.raw_data_dir / "MasterCounts_Adjusted.csv"

    @property
    def raw_counts_all_years(self) -> Path:
        return self.raw_data_dir / "RawCounts_AllYears.csv"


    # CLEAN
    @property
    def clean_data_dir(self) -> Path:
        return self.data_dir / "Clean"

    @property
    def neighborhood_crosswalk(self) -> Path:
        return self.clean_data_dir / "Neighborhood_Crosswalk.csv"

    @property
    def clean_counts_all_years(self) -> Path:
        return self.clean_data_dir / "RawCounts_AllYears_clean.csv"

    @property
    def clean_master_counts_adjusted(self) -> Path:
        return self.clean_data_dir / "MasterCounts_Adjusted_clean.csv"

    @property
    def clean_block_map_coverage(self) -> Path:
        return self.clean_data_dir / "BlockMap_Coverage_clean.csv"

    @property
    def clean_block_level_counts(self) -> Path:
        return self.clean_data_dir / "BlockLevel_Counts_clean.csv"




@dataclass
class Variables:

    @property
    def random_seed(self) -> int:
        return 42
