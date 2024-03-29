from dataclasses import dataclass
from typing import List
from Grade import Grade


@dataclass
class Student:
    name: str
    grades: List[Grade]
