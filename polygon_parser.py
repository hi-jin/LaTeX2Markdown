from ply import yacc
from ply.yacc import LRParser
from polygon_lexer import tokens, lexer
from polygon_ast import *


def p_description(p):
    """
    description : pbegin paragraphs input output example pend
    """
    p[0] = Description(p[1], p[2], p[3], p[4], p[5])


def p_pbegin(p):
    """
    pbegin : BEGIN attr attr attr attr attr attr NEWLINE
    """
    p[0] = Pbegin(p[3])


def p_pend(p):
    """
    pend : END attr NEWLINE
    """
    p[0] = ("pend", )


def p_input(p):
    """
    input : INPUT NEWLINE paragraphs
    """
    p[0] = Input(p[3])


def p_output(p):
    """
    output : OUTPUT NEWLINE paragraphs
    """
    p[0] = Output(p[3])


def p_example(p):
    """
    example : EXAMPLES NEWLINE BEGIN attr NEWLINE example_files END attr NEWLINE
    """
    p[0] = Example(p[6])


def p_example_file(p):
    """
    example_file : EXAMPLE attr attr text NEWLINE
    """
    p[0] = Example_file(p[2], p[3])


def p_example_files(p):
    """
    example_files   : example_file
                    | example_file example_files
    """
    if len(p) == 2:
        p[0] = (p[1], )
    elif len(p) == 3:
        p[0] = (p[1], *p[2])


def p_attr(p):
    """
    attr : LEFT_BRACE text RIGHT_BRACE
    """
    p[0] = p[2]


def p_paragraph(p):
    """
    paragraph   : NEWLINE
                | math paragraph
                | bold paragraph
                | italic paragraph
                | monospace paragraph
                | text paragraph
    """

    if len(p) == 2:
        p[0] = Paragraph(None)
    elif len(p) == 3:
        if p[2].head is None:
            p[0] = Paragraph(p[1])
        else:
            p[0] = Paragraph(p[1], p[2])


def p_paragraphs(p):
    """
    paragraphs : paragraph
               | paragraph paragraphs
    """
    if len(p) == 2:
        p[0] = (p[1],)
    elif len(p) == 3:
        p[0] = (p[1], *p[2])


def p_text(p):
    """
    text : LETTER
         | LETTER text
    """
    if len(p) == 2:
        p[0] = Text(p[1])
    elif len(p) == 3:
        p[0] = Text(p[1] + p[2].content)


def p_bold(p):
    """
    bold : BOLD attr
    """
    p[0] = Bold(p[2])


def p_italic(p):
    """
    italic : ITALIC attr
    """
    p[0] = ("italic", p[2])


def p_monospace(p):
    """
    monospace : MONOSPACE attr
    """
    p[0] = Monospace(p[2])


def p_math(p):
    """
    math : DOLLAR text DOLLAR
    """
    p[0] = Math(p[2])


def p_error(p):
    print(f"Syntax error at '{p.value}'")


parser: LRParser = yacc.yacc()

# file = open("./input_files/seq-comp/test.tex", "r", encoding="utf-8")
# text = file.read()

# ast = parser.parse(text)
# print(ast)
