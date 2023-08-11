from __future__ import annotations
from typing import Tuple


class Description:
    __match_args__ = ('paragraphs', )

    def __init__(self, paragraphs: Tuple[Paragraph]):
        self.paragraphs = paragraphs

    def __add__(self, other: Description) -> Description:
        return Description(self.paragraphs + other.paragraphs)

    def __repr__(self):
        return f'Description{self.paragraphs!r}'


class Paragraph:
    __match_args__ = ('texts', )

    def __init__(self, texts: Tuple[Text | Bold | Italic | Monospace | Math | Begin | End]):
        self.texts = texts

    def __add__(self, other: Paragraph) -> Paragraph:
        return Paragraph(self.texts + other.texts)

    def __repr__(self):
        return f'Paragraph{self.texts!r}'


class Text:
    __match_args__ = ('content', )

    def __init__(self, content: str):
        self.content = content

    def __add__(self, other: Text) -> Text:
        return Text(self.content + other.content)

    def __repr__(self):
        return f'{self.content!r}'


class Bold:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Bold({self.text!r})'


class Italic:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Italic({self.text!r})'


class Monospace:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Monospace({self.text!r})'


class Math:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Math({self.text!r})'


class Begin:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Begin({self.text!r})'


class End:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'End({self.text!r})'


class Graphic:
    __match_args__ = ('text', )

    def __init__(self, text: Text):
        self.text = text

    def __repr__(self):
        return f'Graphic({self.text!r})'
