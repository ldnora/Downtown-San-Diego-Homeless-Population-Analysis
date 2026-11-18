"""
This file contains the unified configuration of paths used to save and load data.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Config:
    root_dir: Path = Path(__file__).resolve().parents[1]

    @property
    def data_dir(self) -> Path:
        return self.root_dir / "Data"

    @property
    def raw_data_dir(self) -> Path:
        return self.data_dir / "Raw"

    @property
    def block_level_counts(self) -> Path:
        return self.raw_data_dir / "BlockLevel_Counts.csv"

    @property
    def block_map_coverage(self) -> Path:
        return self.raw_data_dir / "BlockMap_Coverage.csv"

    @property
    def downtown_block_grid(self) -> Path:
        return self.raw_data_dir / "Downtown_BlockGrid.csv"

    @property
    def downtown_block_grid_geojson(self) -> Path:
        return self.raw_data_dir / "Downtown_BlockGrid.geojson"

    @property
    def master_counts_adjusted(self) -> Path:
        return self.raw_data_dir / "MasterCounts_Adjusted.csv"

    @property
    def RawCounts_AllYears(self) -> Path:
        return self.raw_data_dir / "RawCounts_AllYears.csv"

    @property
    def cleaned_data_dir(self) -> Path:
        return self.data_dir / "Clean"

    @property
    def reports_dir(self) -> Path:
        return self.root_dir / "Reports"

    random_seed: int = 42
