from ply import lex
from ply.lex import Lexer

tokens = (
    "BEGIN",
    "END",
    "INPUT",
    "OUTPUT",
    "EXAMPLES",
    "EXAMPLE",
    "BOLD",
    "ITALIC",
    "MONOSPACE",
    "IMAGE",
    "DOLLAR",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "NEWLINE",
    "LETTER",
)


def t_BEGIN(t):
    r"\\begin"
    return t


def t_END(t):
    r"\\end"
    return t


def t_INPUT(t):
    r"\\InputFile"
    return t


def t_OUTPUT(t):
    r"\\OutputFile"
    return t


def t_EXAMPLES(t):
    r"\\Examples"
    return t


def t_EXAMPLE(t):
    r"\\exmpfile"
    return t


def t_BOLD(t):
    r"\\bf"
    return t


def t_ITALIC(t):
    r"\\it"
    return t


def t_MONOSPACE(t):
    r"\\t"
    return t


"""
def t_IMAGE(t):
    r"\\Image"
    return t
"""


def t_DOLLAR(t):
    r"\$"
    return t


def t_LEFT_BRACE(t):
    r"{"
    return t


def t_RIGHT_BRACE(t):
    r"}"
    return t


def t_NEWLINE(t):
    r"\n+"
    return t


def t_LETTER(t):
    r"."
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer: Lexer = lex.lex()
