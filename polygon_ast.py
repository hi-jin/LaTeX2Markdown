from __future__ import annotations
from typing import Tuple


class Description:
    __match_args__ = ('pbegin', 'legend', 'input', 'output', 'example')

    def __init__(self, pbegin: Pbegin, legend: Tuple[Paragraph], input: Input, output: Output, example: Example):
        self.pbegin = pbegin
        self.legend = legend
        self.input = input
        self.output = output
        self.example = example

    def __repr__(self):
        return f'Description({self.pbegin!r}, {self.legend!r}, {self.input!r}, {self.output!r}, {self.example!r})'


class Pbegin:
    __match_args__ = ('problem_name', )

    def __init__(self, problem_name):
        self.problem_name = problem_name

    def __repr__(self):
        return f'Pbegin({self.problem_name!r})'


class Input:
    __match_args__ = ('paragraphs', )

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs

    def __repr__(self):
        return f'Input({self.paragraphs!r})'


class Output:
    __match_args__ = ('paragraphs', )

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs

    def __repr__(self):
        return f'Output({self.paragraphs!r})'


class Example:
    __match_args__ = ('example_files', )

    def __init__(self, example_files):
        self.example_files = example_files

    def __repr__(self):
        return f'Example({self.example_files!r})'


class Example_file:
    __match_args__ = ('input', 'output')

    def __init__(self, input: Text, output: Text):
        self.input = input
        self.output = output

    def __repr__(self):
        return f'Example_file({self.input!r}, {self.output!r})'


class Note:
    __match_args__ = ('paragraphs', )

    def __init__(self, paragraphs):
        self.paragraphs = paragraphs

    def __repr__(self):
        return f'Note({self.paragraphs!r})'


class Paragraph:
    __match_args__ = ('head', 'paragraph')

    def __init__(self, head, paragraph=None):
        self.head = head
        self.paragraph = paragraph

    def __repr__(self):
        if not self.paragraph:
            return f'Paragraph({self.head!r})'
        else:
            return f'Paragraph({self.head!r}, {self.paragraph!r})'


class Text:
    __match_args__ = ('content', )

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'Text({self.content!r})'


class Bold:
    __match_args__ = ('content', )

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'Bold({self.content!r})'


class Italic:
    __match_args__ = ('content', )

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'Italic({self.content!r})'


class Monospace:
    __match_args__ = ('content', )

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'Monospace({self.content!r})'


class Math:
    __match_args__ = ('content', )

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'Math({self.content!r})'
