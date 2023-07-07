from ply import yacc
from latex_lexer import tokens, lexer
from latex_ast import *


def p_LATEX(p):
    """
    LATEX : EXPR
    """
    p[0] = LATEX(p[1])


def p_STRING(p):
    """
    STRING : CHARACTER
           | CHARACTER STRING
    """
    if len(p) == 2:
        p[0] = STRING(p[1])
    elif len(p) == 3:
        p[0] = STRING(p[1] + p[2].string)


def p_PHRASE(p):
    """
    PHRASE : CHARACTER
           | BRACE_PHRASE
           | BOLD_PHRASE
           | MONOSPACE_PHRASE
           | ITALIC_PHRASE
           | UNDERSCORE_PHRASE
    """
    p[0] = PHRASE(p[1])


def p_BRACE_PHRASE(p):
    """
    BRACE_PHRASE : LEFT_BRACE EXPR RIGHT_BRACE
    """
    p[0] = BRACE_PHRASE(p[2])


def p_BOLD_PHRASE(p):
    """
    BOLD_PHRASE : BOLD PHRASE
    """
    p[0] = BOLD_PHRASE(p[2])


def p_MONOSPACE_PHRASE(p):
    """
    MONOSPACE_PHRASE : MONOSPACE PHRASE
    """
    p[0] = MONOSPACE_PHRASE(p[2])
    

def p_ITALIC_PHRASE(p):
    """
    ITALIC_PHRASE : ITALIC PHRASE
    """
    p[0] = ITALIC_PHRASE(p[2])


def p_UNDERSCORE_PHRASE(p):
    """
    UNDERSCORE_PHRASE : UNDERSCORE PHRASE
    """
    p[0] = UNDERSCORE_PHRASE(p[2])


def p_EXPR_LIST(p):
    """
    EXPR_LIST : EXPR
              | EXPR EXPR_LIST
    """
    if len(p) == 2:
        p[0] = EXPR_LIST([p[1]])
    elif len(p) == 3:
        p[0] = EXPR_LIST([p[1], *p[2].expr_list])


def p_EXPR(p):
    """
    EXPR : EXPR_LIST
         | BEGIN_EXPR
         | STRING
         | PHRASE
         | MATH
         | INPUT_FILE_EXPR
         | OUTPUT_FILE_EXPR
    """
    p[0] = EXPR(p[1])


def p_BEGIN_EXPR(p):
    """
    BEGIN_EXPR : BEGIN BRACE_PHRASE_LIST_FOR_BEGIN
    """
    p[0] = STRING("# " + p[2].string + "\n## 문제")


def p_INPUT_FILE_EXPR(p):
    """
    INPUT_FILE_EXPR : INPUT_FILE
    """
    p[0] = STRING("## 입력")


def p_OUTPUT_FILE_EXPR(p):
    """
    OUTPUT_FILE_EXPR : OUTPUT_FILE
    """
    p[0] = STRING("## 출력")


def p_BRACE_PHRASE_LIST_FOR_BEGIN(p):
    """
    BRACE_PHRASE_LIST_FOR_BEGIN : BRACE_PHRASE BRACE_PHRASE
                                | BRACE_PHRASE BRACE_PHRASE BRACE_PHRASE_LIST_FOR_BEGIN
    """
    p[0] = STRING(p[2].expr.child.string)


def p_MATH(p):
    """
    MATH : DOLLAR MATH_STRING DOLLAR
    """
    p[0] = MATH(p[2].string)


def p_MATH_STRING(p):
    """
    MATH_STRING : STRING
                | UNDERSCORE
                | MATH_STRING MATH_STRING
    """
    if len(p) == 2:
        if isinstance(p[1], STRING):
            p[0] = STRING(p[1].string)
        else:
            p[0] = STRING("_")
    elif len(p) == 3:
        p[0] = STRING(p[1].string + p[2].string)


def p_error(p):
    raise SyntaxError(f"Unexpected token {p}")


parser = yacc.yacc(start="LATEX")
