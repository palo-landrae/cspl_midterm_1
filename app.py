import math
from typing import List

import pandas as pd
from classes.GradeStatisticsCalculator import GradeStatisticsCalculator


def calculate_period_stats(grades: List[float]) -> dict:
    calculator = GradeStatisticsCalculator()
    stats = {
        "mean": calculator.calculate_mean(grades),
        "median": calculator.calculate_median(grades),
        "mode": calculator.calculate_mode(grades),
        "range": calculator.calculate_range(grades),
        "variance": calculator.calculate_variance(grades),
        "standard_deviation": calculator.calculate_standard_deviation(grades),
    }
    return stats


def process_period_data(df: pd.DataFrame) -> pd.DataFrame:
    prelim_stats = calculate_period_stats(df['prelim'].astype(float).tolist())
    midterm_stats = calculate_period_stats(
        df['midterm'].astype(float).tolist())
    finals_stats = calculate_period_stats(df['finals'].astype(float).tolist())

    period_stats = pd.DataFrame.from_dict(
        {'Statistics': list(prelim_stats.keys()),
         'Prelim': list(prelim_stats.values()),
         'Midterm': list(midterm_stats.values()),
         'Finals': list(finals_stats.values())}
    )
    return period_stats


def process_student_data(df: pd.DataFrame) -> pd.DataFrame:
    student_stats = pd.DataFrame(
        columns=['Student Name', 'Prelim', 'Midterm', 'Finals', 'Final Average'])

    calculator = GradeStatisticsCalculator()

    for i, row in df.iterrows():
        prelim_grade = math.floor(float(row['prelim']))
        midterm_grade = math.floor(float(row['midterm']))
        finals_grade = math.floor(float(row['finals']))

        final_average = calculator.calculate_final_average(
            [prelim_grade, midterm_grade, finals_grade])

        student_stats.loc[i] = {
            'Student Name': row['student_name'],
            'Prelim': prelim_grade,
            'Midterm': midterm_grade,
            'Finals': finals_grade,
            'Final Average': final_average
        }
    return student_stats


if __name__ == "__main__":
    df = pd.read_csv("data/students.csv", sep=";")

    period_stats = process_period_data(df)
    print("\nPeriod Statistics:")
    print(period_stats)

    student_stats = process_student_data(df)
    print("\nStudent Statistics:")
    print(student_stats)
