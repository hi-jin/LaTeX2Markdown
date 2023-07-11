from translate import translate

import os
import argparse


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path", help="path of the problem description")

    args = argparser.parse_args()
    path = args.path

    problem_name = os.path.basename(os.path.normpath(path))
    if not problem_name:
        problem_name = os.path.basename(
            os.path.normpath(os.path.split(path)[0]))

    file = open(os.path.join(path, "problem.tex"), "r", encoding="utf-8")
    text = file.read()

    file = open(os.path.join(
        "./output_files", f"{problem_name}.md"), "w", encoding="utf-8")

    file.write(translate(text, path))
    file.write("\n")
    file.close()
