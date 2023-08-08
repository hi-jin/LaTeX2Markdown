from __future__ import annotations
from statement import Statement
from solution import Solution
from typing import Tuple, Dict
import os
import json


class Problem:
    def __init__(self, name: str, statement: Statement, images: Dict[str, str], tutorial: Tuple[str], solutions: Tuple[Solution]):
        self.name = name
        self.statement = statement
        self.images = images
        self.tutorial = tutorial
        self.solutions = solutions

    @staticmethod
    def from_path(path: str) -> Problem:
        name = os.path.basename(path)

        problem_properties_path = os.path.join(
            path, 'statements', 'korean', 'problem-properties.json')

        with open(problem_properties_path, "r", encoding='utf-8') as f:
            d = json.load(f)
            statement = Statement.from_dict(d)

        images = {}
        image_path = os.path.join(path, 'statements', 'korean')

        for root, dirs, files in os.walk(image_path):
            for file in files:
                if file.endswith(".png"):
                    images[file] = os.path.join(root, file)

        tutorial = ()

        solutions = ()

        return Problem(name, statement, images, tutorial, solutions)
