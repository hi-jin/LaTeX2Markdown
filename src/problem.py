from __future__ import annotations
from statement import Statement
from solution import Solution
from typing import Tuple, Dict
import os
import json


class Problem:
    def __init__(self, name: str, statement: Statement, images: Dict[str, str], solutions: Tuple[Solution], tags: Tuple[str], difficulty: Tuple[str]):
        self.name = name
        self.statement = statement
        self.images = images
        self.solutions = solutions
        self.tags = tags
        self.difficulty = difficulty

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

        solutions = ()
        solution_path = os.path.join(path, 'solutions')

        for root, dirs, files in os.walk(solution_path):
            for file in files:
                if file.endswith(".py") or file.endswith(".java"):
                    solutions += (Solution(os.path.join(root, file)),)

        tags = ()
        tags_path = os.path.join(path, 'tags')

        tier = 'bronze'
        level = 'easy'

        with open(tags_path, "r", encoding='utf-8') as f:
            for tag in f.readlines():
                tag = tag.strip()

                if tag in ('bronze', 'silver', 'gold', 'platinum', 'diamond', 'ruby'):
                    tier = tag
                elif tag in ('easy', 'medium', 'hard'):
                    level = tag
                else:
                    tags += (tag,)

        return Problem(name, statement, images, solutions, tags, (tier, level))
