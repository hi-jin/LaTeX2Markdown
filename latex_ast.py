class LATEX:
    __match_args__ = ("expr", )
    
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"LATEX({self.expr!r})"


class STRING:
    __match_args__ = ("string", )
    
    def __init__(self, string):
        self.string = string
    
    def __repr__(self):
        return f"STRING({self.string!r})"


class BRACE_PHRASE:
    __match_args__ = ("expr", )
    
    def __init__(self, expr):
        self.expr = expr
    
    def __repr__(self):
        return f"BRACE_PHRASE({self.expr!r})"


class BOLD_PHRASE:
    __match_args__ = ("phrase", )
    
    def __init__(self, phrase):
        self.phrase = phrase
    
    def __repr__(self):
        return f"BOLD_PHRASE({self.phrase!r})"


class MONOSPACE_PHRASE:
    __match_args__ = ("phrase", )
    
    def __init__(self, phrase):
        self.phrase = phrase
    
    def __repr__(self):
        return f"MONOSPACE_PHRASE({self.phrase!r})"


class ITALIC_PHRASE:
    __match_args__ = ("phrase", )
    
    def __init__(self, phrase):
        self.phrase = phrase
    
    def __repr__(self):
        return f"ITALIC_PHRASE({self.phrase!r})"


class UNDERSCORE_PHRASE:
    __match_args__ = ("phrase", )
    
    def __init__(self, phrase):
        self.phrase = phrase
    
    def __repr__(self):
        return f"UNDERSCORE_PHRASE({self.phrase!r})"


class PHRASE:
    __match_args__ = ("child", )
    
    def __init__(self, child):
        self.child = child
        
    def __repr__(self):
        return f"PHRASE({self.child!r})"


class EXPR_LIST:
    __match_args__ = ("expr_list", )
    
    def __init__(self, expr_list):
        self.expr_list = expr_list

    def __repr__(self):
        return f"EXPR_LIST({', '.join([repr(expr) for expr in self.expr_list])})"


class EXPR:
    __match_args__ = ("child", )
    
    def __init__(self, child):
        self.child = child
    
    def __repr__(self):
        return f"EXPR({self.child!r})"


class MATH:
    __match_args__ = ("string", )
    
    def __init__(self, string):
        self.string = string
    
    def __repr__(self):
        return f"MATH({self.string})"
