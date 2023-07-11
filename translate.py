from polygon_parser import parser
from polygon_ast import *
from latex_encoder import encode

import re

example_path = "./example_files/"


def translate(text, path):
    global example_path
    example_path = path

    ast = parser.parse(text)
    return interp(ast)


def interp(node):
    match node:
        case Description(pbegin, legend, input, output, example):
            return '\n\n'.join((
                f"# {interp(pbegin)}",
                f"## 문제",
                '\n\n'.join(map(interp, legend)),
                f"## 입력",
                f"{interp(input)}",
                f"## 출력",
                f"{interp(output)}",
                f"{interp(example)}",
            ))
        case Pbegin(problem_name):
            return interp(problem_name)
        case Text(content):
            return content
        case Paragraph(head, tail):
            return interp(head) + (interp(tail) if tail else '')
        case Bold(text):
            return f"**{interp(text)}**"
        case Italic(text):
            return f"*{interp(text)}*"
        case Monospace(text):
            return f"`{interp(text)}`"
        case Math(text):
            return f'![](data:image/svg+xml;base64,{encode(interp(text))})'
        case Input(paragraphs):
            return '\n\n'.join(map(interp, paragraphs))
        case Output(paragraphs):
            return '\n\n'.join(map(interp, paragraphs))
        case Example(example_files):
            return '\n\n'.join(map(interp, example_files))
        case Example_file(input, output):
            input, output = map(interp, (input, output))

            m = re.search(r"(\d+)", input)
            i = int(m.group(1)) if m else 0

            input = open(example_path + input, "r", encoding='utf-8').read()
            output = open(example_path + output, "r", encoding='utf-8').read()

            return '\n\n'.join(
                (
                    f"## 예제 입력 {i}",
                    ''.join((
                        f"```\n",
                        f"{input}",
                        f"```"
                    )),
                    f"## 예제 출력 {i}",
                    ''.join((
                        f"```\n",
                        f"{output}",
                        f"```"
                    )),
                )
            )
