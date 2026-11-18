from config import Datasets
import pandas as pd
from pathlib import Path


class Standardizer:

    @staticmethod
    def date(df: pd.DataFrame) -> pd.DataFrame:
        month_mapping = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "June": "06",
            "July": "07",
            "Aug": "08",
            "Sept": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        df = df.copy()

        df['date'] = pd.to_datetime({
            'year': df['year'],
            'month': df['month'].replace(month_mapping),
            'day': 1
        })

        return df.drop(columns=['year', 'month'])

    @staticmethod
    def date_iso_format(df: pd.DataFrame) -> pd.DataFrame:
        df['count_date'] = (
            df['count_date']
            .astype(str)
            .str.replace('"', '', regex=False)
            .str.strip()
        )

        df['count_date'] = pd.to_datetime(df['count_date'], format="%Y-%m-%d")

        return df

    @staticmethod
    def convert_to_int(df: pd.DataFrame) -> pd.DataFrame:
        df['tents_structures'] = df['tents_structures'].astype(int)

        return df

    @staticmethod
    def null_handling_nulls_of_tents_structures(df: pd.DataFrame) -> pd.DataFrame:
        df['tents_structures'] = (
            df.groupby('block_id')['tents_structures']
            .transform(lambda x: x.fillna(x.median()))
        )

        return df

    @staticmethod
    def neighborhood_vocabularies(df: pd.DataFrame) -> pd.DataFrame:
        pass

    @staticmethod
    def save(df: pd.DataFrame, output_path: Path) -> None:
        df.to_csv(output_path, index=False)


def main():
    datasets = Datasets()

    raw_counts = pd.read_csv(datasets.raw_counts_all_years)
    adjusted_counts = pd.read_csv(datasets.raw_master_counts_adjusted)
    block_coverage = pd.read_csv(datasets.raw_block_map_coverage)
    block_level_counts = pd.read_csv(datasets.raw_block_level_counts)

    raw_counts = Standardizer.date(raw_counts)
    adjusted_counts = Standardizer.date(adjusted_counts)
    block_coverage = Standardizer.date(block_coverage)

    block_level_counts = Standardizer.date_iso_format(block_level_counts)
    block_level_counts = Standardizer.null_handling_nulls_of_tents_structures(
        block_level_counts)
    block_level_counts = Standardizer.convert_to_int(block_level_counts)

    Standardizer.save(raw_counts, datasets.clean_counts_all_years)
    Standardizer.save(adjusted_counts, datasets.clean_master_counts_adjusted)
    Standardizer.save(block_coverage, datasets.clean_block_map_coverage)
    Standardizer.save(block_level_counts, datasets.clean_block_level_counts)


if __name__ == '__main__':
    main()
