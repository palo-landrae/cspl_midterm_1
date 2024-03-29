from typing import List
import math
from collections import Counter


class GradeStatisticsCalculator:
    @staticmethod
    def calculate_mean(grades: List[float]) -> float:
        return sum(grades) / len(grades)

    @staticmethod
    def calculate_median(grades: List[float]) -> float:
        sorted_grades = sorted(grades)
        middle_index = len(sorted_grades) // 2
        if len(sorted_grades) % 2 == 0:
            return (sorted_grades[middle_index - 1] + sorted_grades[middle_index]) / 2.0
        else:
            return sorted_grades[middle_index]

    @staticmethod
    def calculate_mode(grades: List[float]) -> int:
        counts = Counter(grades)
        return max(counts, key=counts.get)  # type: ignore

    @staticmethod
    def calculate_range(grades: List[float]) -> float:
        return max(grades) - min(grades)

    @staticmethod
    def calculate_variance(grades: List[float]) -> float:
        mean = GradeStatisticsCalculator.calculate_mean(grades)
        sum_of_squares = sum((grade - mean) ** 2 for grade in grades)
        return sum_of_squares / len(grades)

    @staticmethod
    def calculate_standard_deviation(grades: List[float]) -> float:
        return math.sqrt(GradeStatisticsCalculator.calculate_variance(grades))

    @staticmethod
    def calculate_final_average(grades: List[float]) -> float:
        return math.ceil(grades[0] * 0.3 + grades[1] * 0.3 + grades[2] * 0.4)
