from ply import yacc
from ply.yacc import LRParser
from description.lexer import tokens, lexer
from description.ast import *


def p_description(p):
    '''
    description : paragraph
                | paragraph NEWLINE
                | paragraph NEWLINE description
    '''

    if len(p) == 2 or len(p) == 3:
        p[0] = Description((p[1], ))
    elif len(p) == 4:
        p[0] = Description((p[1], )) + p[3]


def p_paragraph(p):
    '''
    paragraph   : math
                | bold
                | italic
                | monospace
                | graphic
                | text
                | math paragraph
                | bold paragraph
                | italic paragraph
                | monospace paragraph
                | graphic paragraph
                | text paragraph
    '''

    if len(p) == 2:
        p[0] = Paragraph((p[1], ))
    elif len(p) == 3:
        p[0] = Paragraph((p[1], )) + p[2]


def p_text(p):
    '''
    text : LETTER
         | LETTER text
    '''

    if len(p) == 2:
        p[0] = Text(p[1])
    elif len(p) == 3:
        p[0] = Text(p[1]) + p[2]


def p_bold(p):
    '''
    bold : BOLD LEFT_BRACE text RIGHT_BRACE
    '''

    p[0] = Bold(p[3])


def p_italic(p):
    '''
    italic : ITALIC LEFT_BRACE text RIGHT_BRACE
    '''

    p[0] = Italic(p[3])


def p_monospace(p):
    '''
    monospace : MONOSPACE LEFT_BRACE text RIGHT_BRACE
    '''

    p[0] = Monospace(p[3])


def p_math(p):
    '''
    math : DOLLAR text DOLLAR
    '''

    p[0] = Math(p[2])


def p_begin(p):
    '''
    begin : BEGIN LEFT_BRACE text RIGHT_BRACE
    '''

    p[0] = Begin(p[3])


def p_end(p):
    '''
    end : END LEFT_BRACE text RIGHT_BRACE
    '''

    p[0] = End(p[3])


def p_graphic(p):
    '''
    graphic : begin NEWLINE text GRAPHIC LEFT_BRACE text RIGHT_BRACE text NEWLINE end
    '''

    p[0] = Graphic(p[6])


def p_error(p):
    line_number = p.lexer.lineno
    char_position = p.lexer.lexpos
    print("Syntax error at line", line_number, "character", char_position)
    print(f"Syntax error at '{p.value}'")


parser: LRParser = yacc.yacc()


def parse(latex: str) -> Description:
    return parser.parse(latex, lexer=lexer)
