import os
import pandas as pd


def read_dataset(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def pull_40_random_sample(df: pd.DataFrame, output_folder: str) -> None:
    sample = (
        df.sample(n=40, random_state=42)
        .sort_values(
            by=["year", "month", "area", "component"]
        )
        .reset_index(drop=True)
    )

    sample['status'] = ''
    sample.to_csv(f"{output_folder}random_sample_validation.csv", index=False)


def underestand_area(df: pd.DataFrame) -> None:
    sub_area = df.query('area_type == "sub-area"')
    print(sub_area.area.unique())


def check_sum_east_village(df: pd.DataFrame, output_folder: str) -> None:
    east_village = df.query('area == "East Village"')

    east_village_subareas = (
        df.query('area_type == "sub-area"')
        .groupby(['year', 'month', 'component'])['count']
        .sum()
        .reset_index()
    )

    comparison = east_village.merge(
        east_village_subareas,
        on=['year', 'month', 'component'],
        suffixes=('_neighborhood', '_subareas')
    )

    comparison['difference'] = (
        comparison['count_neighborhood'] -
        comparison['count_subareas']
    )

    comparison.to_csv(
        f'{output_folder}check_sum_east_village.csv', index=False)


def determinate_the_core(df: pd.DataFrame) -> None:
    core = df.query('area == "Core"')
    print(core.year.unique())


def calculate_error_rate(df: pd.DataFrame) -> None:
    not_ok_ctn = df.query('status != "ok"')

    error_rate = (not_ok_ctn.shape[0] / df.shape[0]) * 100

    print(not_ok_ctn)
    print(f'The error rate is: {error_rate:.2f}%')


def main():
    output_folder = "Tasks/Assignment 1: Data Validation, Cleaning & Standardization/1.1 Validate delivered count data against source reports/output/"
    os.makedirs(output_folder, exist_ok=True)

    df = read_dataset("Data/RawCounts_AllYears.csv")

    # commented because it's finished
    # underestand_area(df)
    # pull_40_random_sample(df, output_folder)
    # check_sum_east_village(df, output_folder)
    # determinate_the_core(df)

    calculate_error_rate(read_dataset(
        'Tasks/Assignment 1: Data Validation, Cleaning & Standardization/1.1 Validate delivered count data against source reports/output/random_sample_validation.csv'))


if __name__ == '__main__':
    main()
