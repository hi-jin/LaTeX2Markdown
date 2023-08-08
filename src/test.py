import os
import json
from problem import Problem
from programmers.translate import translate
from sys import argv

if __name__ == "__main__":
    path = os.path.normpath(argv[1])
    subdirs = [os.path.join(path, name) for name in os.listdir(
        path) if os.path.isdir(os.path.join(path, name))]

    for problem_path in subdirs:
        problem = Problem.from_path(problem_path)

        print(problem.name)
        output = translate(problem)

        statement_path = os.path.join(problem_path, 'statements', 'korean')
        with open(os.path.join(statement_path, f'{problem.name}.md'), "w", encoding='utf-8') as f:
            f.write(output)
