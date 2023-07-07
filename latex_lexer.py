from ply import lex
from functools import reduce


tokens = (
    "BEGIN",
    "BOLD",
    "MONOSPACE",
    "ITALIC",
    "INPUT_FILE",
    "OUTPUT_FILE",
    "DOLLAR",
    "UNDERSCORE",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "CHARACTER",
    "EOF",
)


def t_BEGIN(t):
    r"\\begin"
    return t

def t_BOLD(t):
    r"\\bf"
    return t

def t_MONOSPACE(t):
    r"\\t"
    return t

def t_ITALIC(t):
    r"\\it"
    return t

def t_INPUT_FILE(t):
    r"\\InputFile"
    return t

def t_OUTPUT_FILE(t):
    r"\\OutputFile"
    return t

def t_DOLLAR(t):
    r"\$"
    return t

def t_UNDERSCORE(t):
    r"_"
    return t

def t_LEFT_BRACE(t):
    r"{"
    return t

def t_RIGHT_BRACE(t):
    r"}"
    return t

def t_CHARACTER(t):
    r"(. | \n)"
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0]) # type: ignore
    t.lexer.skip(1)


lexer = lex.lex()
