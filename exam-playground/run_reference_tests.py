import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
passed = []
failed = []

for topic in sorted(
    path for path in root.iterdir()
    if path.is_dir() and path.name != '_solutions'
):
    for question in sorted(
        path for path in topic.iterdir()
        if path.is_dir() and path.name.startswith('Q')
        and (path / 'Solution.java').exists()
    ):
        reference = root / '_solutions' / topic.name / question.name / 'Solution.java'
        input_file = question / 'testcases' / 'input1.txt'
        expected_file = question / 'testcases' / 'expected1.txt'
        compile_result = subprocess.run(
            ['javac', str(reference)], capture_output=True, text=True
        )
        if compile_result.returncode != 0:
            failed.append((question.name, 'compile error'))
            continue

        run_result = subprocess.run(
            ['java', '-cp', str(reference.parent), 'Solution'],
            input=input_file.read_text(encoding='utf-8'),
            capture_output=True,
            text=True,
        )
        actual = run_result.stdout.strip()
        expected = expected_file.read_text(encoding='utf-8').strip()
        if run_result.returncode == 0 and actual == expected:
            passed.append(question.name)
        else:
            failed.append((question.name, actual, expected))

print(f'Total: {len(passed) + len(failed)}')
print(f'Passed: {len(passed)}')
print(f'Failed: {len(failed)}')
for failure in failed:
    print(f'FAIL: {failure[0]}')
