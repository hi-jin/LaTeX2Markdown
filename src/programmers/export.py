import os
from problem import Problem


def export_tests(problem: Problem, path: str):
    for input_file_path, output_file_path in problem.tests:
        input_file_name, input_ext = os.path.splitext(
            os.path.basename(input_file_path))
        output_file_name, output_ext = os.path.splitext(
            os.path.basename(output_file_path))

        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            with open(f"{path}/{input_file_name}.in.txt", 'w', newline='\n', encoding='utf-8') as f:
                f.write(input_file.read())

        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            with open(f"{path}/{output_file_name}.out.txt", 'w', newline='\n', encoding='utf-8') as f:
                f.write(output_file.read())
