import base64
from typing import Dict
from programmers.latex2svg import latex2svg
from problem import Problem
from description.ast import *
from description.parser import parse


def translate(problem: Problem) -> str:
    test = '\n\n'.join(
        (
            '\n\n'.join(
                (
                    f"## 예제 입력 {i}",
                    ''.join(
                        (
                            f"```\n",
                            f"{input}",
                            f"```"
                        )
                    ),
                    f"## 예제 출력 {i}",
                    ''.join(
                        (
                            f"```\n",
                            f"{output}",
                            f"```"
                        )
                    )
                )
            )
        ) for i, (input, output) in enumerate(problem.statement.tests, 1)
    )

    return '\n\n'.join((
        f"# {problem.statement.name}",
        f"## 문제",
        interp(parse(problem.statement.legend), problem.images),
        f"## 입력",
        interp(parse(problem.statement.input), problem.images),
        f"## 출력",
        interp(parse(problem.statement.output), problem.images),
        test,
    ))


def interp(node, images: Dict[str, str]):
    match node:
        case Description(paragraphs):
            return '\n\n'.join(interp(paragraph, images) for paragraph in paragraphs)
        case Paragraph(texts):
            return ''.join(interp(text, images) for text in texts)
        case Text(content):
            return content
        case Bold(text):
            return f"**{interp(text, images)}**"
        case Italic(text):
            return f"*{interp(text, images)}*"
        case Monospace(text):
            return f"`{interp(text, images)}`"
        case Math(text):
            return f'![](data:image/svg+xml;base64,{encode_math(interp(text, images))})'
        case Graphic(text):
            return f'![](data:image/png;base64,{encode_img(images[interp(text, images)])})'


def encode_math(math: str):
    '''
    Encodes a LaTeX math into svg
    Encodes a svg into base64.
    '''

    svg = latex2svg(r'$\textcolor{white}{' + math + '}$')['svg']
    return svg2base64(svg)


def svg2base64(svg: str):
    svg_bytes = svg.encode('utf-8')
    base64_encoded = base64.b64encode(svg_bytes)
    base64_string = base64_encoded.decode('utf-8')

    return base64_string


def encode_img(img_path: str):
    with open(img_path, "rb") as f:
        img_bytes = f.read()
        base64_encoded = base64.b64encode(img_bytes)
        base64_string = base64_encoded.decode('utf-8')

        return base64_string
