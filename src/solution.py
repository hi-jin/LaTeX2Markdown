import os


class Solution:
    def __init__(self, path: str):
        name, ext = os.path.splitext(os.path.basename(path))

        self.name = name

        if ext == '.py':
            self.language = 'python'
        elif ext == '.java':
            self.language = 'java'

        with open(path, 'r', encoding='utf-8') as f:
            self.code = f.read()
