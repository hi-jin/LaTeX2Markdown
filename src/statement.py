from __future__ import annotations
from description.ast import Description
from description.parser import parse
from typing import Tuple
import json


class Statement:
    def __init__(self, name: str, legend: Description, input: Description, output: Description, tests: Tuple[Test]):
        self.name = name
        self.legend = legend
        self.input = input
        self.output = output
        self.tests = tests

    @staticmethod
    def from_dict(d: dict) -> Statement:
        return Statement(
            d['name'],
            parse(d['legend']),
            parse(d['input']),
            parse(d['output']),
            tuple(Test.from_dict(test) for test in d['sampleTests'])
        )

    def __repr__(self) -> str:
        return json.dumps({
            'name': self.name,
            'legend': repr(self.legend),
            'input': repr(self.input),
            'output': repr(self.output),
            'sampleTests': tuple(test.to_dict() for test in self.tests)
        }, indent=4, ensure_ascii=False)


class Test:
    def __init__(self, input: str, output: str):
        self.input = input
        self.output = output

    @ staticmethod
    def from_dict(d: dict) -> Test:
        return Test(d['input'], d['output'])

    def to_dict(self) -> dict:
        return {
            'input': self.input,
            'output': self.output
        }

    def __repr__(self) -> str:
        return json.dumps({
            'input': self.input,
            'output': self.output
        }, indent=4)
