import re
from problem import Problem

abstract_template = '''\\section{{{title}}}

\\begin{{frame}} % No title at first slide
    \\sectiontitlenonumber{{{title}}}
    \\sectionmeta{{
        \\texttt{{{tags}}}\\\\
        난이도 -- \\textbf{{\\color{{{ac_color}}}{difficulty}}}
    }}
    \\begin{{itemize}}
        {notes}
    \\end{{itemize}}
\\end{{frame}}
'''


def abstract(problem: Problem):
    tags = ', '.join(problem.tags)

    ac_color = f'ac{problem.difficulty[0]}'
    difficulty = problem.difficulty[1]
    difficulty = difficulty[0].upper() + difficulty[1:]

    notes = '\n\t\t'.join(
        f'\\item {note}' for note in problem.statement.notes.split('\r\n'))

    return abstract_template.format(title=problem.statement.name, tags=tags, ac_color=ac_color,
                                    difficulty=difficulty, notes=notes)


statement_template = '''\\begin{{frame}}{{{title}}}
{statement}
\\end{{frame}}
'''

constraints_template = '''\\begin{{frame}}{{{title} 입출력}}
{statement}
\\end{{frame}}
'''

test_template = '''\\begin{{frame}}[fragile]{{{title} 예제 입출력}}
\\begin{{minted}}[linenos,fontsize=\scriptsize,frame=single]{{text}}
{tests}
\end{{minted}}
\end{{frame}}
'''


def statement(problem: Problem):
    return '\n\n'.join((
        statement_template.format(
            title=problem.statement.name, statement=problem.statement.legend),
        constraints_template.format(
            title=problem.statement.name, statement='\n\n'.join(
                (problem.statement.input, problem.statement.output))
        ),
        test_template.format(title=problem.statement.name, tests='\n'.join(
            '->'.join((test.input, test.output)) for test in problem.statement.tests
        )),
    ))


tutorial_template = '''\\begin{{frame}}{{{title} 풀이}}
    \\begin{{itemize}}
        {tutorial}
    \\end{{itemize}}
\\end{{frame}}
'''


def tutorial(problem: Problem):
    items = '\n\t\t'.join(
        f'\\item {note}' for note in problem.statement.tutorial.split('\r\n'))

    return tutorial_template.format(title=problem.statement.name,
                                    tutorial=items)


solution_template = '''\\begin{{frame}}[fragile]{{{title} {language} 정답}}
\\begin{{minted}}[linenos,fontsize=\scriptsize,frame=single]{{{language}}}
{solution}
\\end{{minted}}
\\end{{frame}}
'''


def solution(problem: Problem):
    return '\n\n'.join(solution_template.format(
        title=problem.statement.name,
        language=solution.language,
        solution=solution.code
    ) for solution in problem.solutions)


def set_image_prefix(problem: Problem):
    statement = problem.statement

    pattern = r'\\includegraphics\{(.+?)\.png\}'
    replace_pattern = r'\\includegraphics[width=\\textwidth]{{images/' + \
        problem.name + r'/\1.png}}'

    statement.legend = re.sub(pattern, replace_pattern, statement.legend)
    statement.input = re.sub(pattern, replace_pattern, statement.input)
    statement.output = re.sub(pattern, replace_pattern, statement.output)
    statement.notes = re.sub(pattern, replace_pattern, statement.notes)
    statement.tutorial = re.sub(pattern, replace_pattern, statement.tutorial)


def editorial(problem: Problem) -> str:
    set_image_prefix(problem)

    return '\n\n'.join((
        abstract(problem),
        statement(problem),
        tutorial(problem),
        solution(problem)
    ))
