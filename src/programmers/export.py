import os
import shutil
from problem import Problem


def export_tests(problem: Problem, path: str):
    for input_file_path, output_file_path in problem.tests:
        input_file_name, input_ext = os.path.splitext(
            os.path.basename(input_file_path))
        output_file_name, output_ext = os.path.splitext(
            os.path.basename(output_file_path))

        shutil.copy(input_file_path, os.path.join(
            path, f"{input_file_name}.in.txt"))

        shutil.copy(output_file_path, os.path.join(
            path, f"{output_file_name}.out.txt"))
