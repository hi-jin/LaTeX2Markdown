from translate import translate

import re
import os
import argparse


def get_problem_name(directory: str):
    m = re.match(r'(.*)\-\d+\$linux', directory)

    return m.group(1) if m else directory


def main():
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            problem_name = get_problem_name(directory)
            print(problem_name)
            statement = os.path.join(path, directory, "statements", "korean")

            file = open(os.path.join(statement, "problem.tex"),
                        "r", encoding="utf-8")
            text = file.read()

            file = open(os.path.join(
                statement, f"{problem_name}.md"), "w", encoding="utf-8")

            file.write(translate(text, statement))
            file.write("\n")
            file.close()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path", help="path containing polygon packages")

    args = argparser.parse_args()
    path = args.path
    main()
