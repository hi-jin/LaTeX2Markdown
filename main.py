from polygon_parser import parser
from polygon_ast import *
from latex_encoder import encode

import re
import os
import argparse


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

            input = open(path + input, "r", encoding='utf-8').read()
            output = open(path + output, "r", encoding='utf-8').read()

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


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path", help="path of the problem description")

    args = argparser.parse_args()
    path = args.path

    problem_name = os.path.basename(os.path.normpath(path))
    if not problem_name:
        problem_name = os.path.basename(
            os.path.normpath(os.path.split(path)[0]))

    file = open(os.path.join(path, "problem.tex"), "r", encoding="utf-8")
    text = file.read()

    ast = parser.parse(text)

    file = open(os.path.join(
        "./output_files", f"{problem_name}.md"), "w", encoding="utf-8")
    file.write(interp(ast))
    file.write("\n")
    file.close()
