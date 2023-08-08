import os
import json
from statement import Statement
from sys import argv

if __name__ == "__main__":
    dir = argv[1]

    # find "problem-properties.json" file in directory's descendants
    # and test json parsing
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file == "problem-properties.json":
                with open(os.path.join(root, file), "r", encoding='utf-8') as f:
                    d = json.load(f)
                    s = Statement.from_dict(d)
                    print(s)
