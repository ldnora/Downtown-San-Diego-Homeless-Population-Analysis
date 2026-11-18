import pandas as pd
from config import Datasets


def tents_structures(file):
    df = pd.read_csv(file)

    print(df.tents_structures.describe())
    print(
        f'Count of floats: {(df['tents_structures'].dropna() % 1 != 0).sum()}')

    print(
        f'Count of nulls of tents_structures: {df.tents_structures.isna().sum()}')


def crosswalk():
    datasets = Datasets()

    files = {
        'Block Level Counts': (datasets.raw_block_level_counts, "neighborhood"),
        'Block Map Coverage': (datasets.raw_block_map_coverage, "block"),
        'Downtown Block Grid': (datasets.raw_downtown_block_grid, "neighborhood"),
        'Master Counts Adjusted': (datasets.raw_master_counts_adjusted, "area"),
        'Counts All Years': (datasets.raw_counts_all_years, "area")
    }

    for name, (path, col) in files.items():
        df = pd.read_csv(path)

        print(f"\n== {name} ({col}) ==")
        print(df[col].value_counts(dropna=False).to_string())


def main():
    datasets = Datasets()
    # tents_structures(datasets.clean_block_level_counts)

    crosswalk()


if __name__ == '__main__':
    main()
