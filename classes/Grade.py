from dataclasses import dataclass


@dataclass
class Grade:
    grading_period: str
    value: int
