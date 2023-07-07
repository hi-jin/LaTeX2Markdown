import requests
from latex_parser import parser
from latex_ast import *
import base64
import os


def interp(ast):
    match ast:
        case LATEX(expr):
            return interp(expr)
        case STRING(string):
            return string
        case BRACE_PHRASE(expr):
            return interp(expr)
        case BOLD_PHRASE(phrase):
            return f"**{interp(phrase)}**"
        case MONOSPACE_PHRASE(phrase):
            return f"`{interp(phrase)}`"
        case ITALIC_PHRASE(phrase):
            return f"*{interp(phrase)}*"
        case UNDERSCORE_PHRASE(phrase):
            return f"[{interp(phrase)}]"
        case PHRASE(child):
            return interp(child)
        case EXPR_LIST(expr_list):
            result = ""
            for expr in expr_list:
                result += interp(expr) # type: ignore
            return result
        case EXPR(child):
            return interp(child)
        case MATH(string):
            png = requests.get(f"https://latex.codecogs.com/png.latex?{string}").content
            base64_png = base64.b64encode(png).decode("utf-8")
            return f"![](data:image/png;base64,{base64_png})"


def main():
    input_file_dir = "input_files"
    output_file_dir = "output_files"
    
    input_files = os.listdir(input_file_dir)
    
    for input_file_name in input_files:
        with open(os.path.join(input_file_dir, input_file_name), "r") as f:
            file = f.read()
        
        ast = parser.parse(file)
        md = interp(ast)
        
        output_file = os.path.join(output_file_dir, input_file_name.split(".")[0] + ".md")
        with open(output_file, "w+") as f:
            f.write(md) # type: ignore


if __name__ == "__main__":
    main()
