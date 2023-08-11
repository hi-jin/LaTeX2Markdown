import os
import shutil
from problem import Problem
from editorial import editorial
from programmers.export import export_tests
from programmers.translate import translate


def export(problem: Problem, path: str):
    if not os.path.exists(path):
        os.mkdir(path)

    test_path = os.path.join(path, 'tests')

    if not os.path.exists(test_path):
        os.mkdir(test_path)

    export_tests(problem, test_path)

    new_image_path = os.path.join(path, 'images')

    if not os.path.exists(new_image_path):
        os.mkdir(new_image_path)

    for image_name, image_path in problem.images.items():
        shutil.copy(image_path, os.path.join(new_image_path, image_name))

    solution_path = os.path.join(path, 'solutions')

    if not os.path.exists(solution_path):
        os.mkdir(solution_path)

    for solution in problem.solutions:
        ext = '.py' if solution.language == 'python' else '.java'
        with open(os.path.join(solution_path, f'{solution.name}{ext}'), 'w', encoding='utf-8') as f:
            f.write(solution.code)

    with open(os.path.join(path, f'{problem.name}.md'), 'w', newline='\n', encoding='utf-8') as f:
        f.write(translate(problem))

    with open(os.path.join(path, f'{problem.name}.tex'), 'w', newline='\n', encoding='utf-8') as f:
        f.write(editorial(problem))
