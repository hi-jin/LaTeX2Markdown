from ply import lex
from ply.lex import Lexer

tokens = (
    "BEGIN",
    "END",
    "GRAPHIC",
    "NOTE",
    "BOLD",
    "ITALIC",
    "MONOSPACE",
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


def t_GRAPHIC(t):
    r"\\includegraphics"
    return t


def t_BOLD(t):
    r"\\bf"
    return t


def t_ITALIC(t):
    r"\\it"
    return t


def t_MONOSPACE(t):
    r"(\\texttt)|(\\t)"
    return t


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
    r"((\r\n)|(\\\\))+"
    t.lexer.lineno += len(t.value)

    return t


def t_LETTER(t):
    r"."
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer: Lexer = lex.lex()
