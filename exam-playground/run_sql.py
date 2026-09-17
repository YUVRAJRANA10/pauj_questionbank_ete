import sqlite3
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit('Usage: python run_sql.py <sql-question-folder>')

question_dir = Path(sys.argv[1]).resolve()
schema = question_dir / 'schema.sql'
attempt = question_dir / 'attempt.sql'
expected = question_dir / 'expected_output.txt'
if not schema.exists() or not attempt.exists():
    raise SystemExit('The folder must contain schema.sql and attempt.sql')

database = sqlite3.connect(':memory:')
database.executescript(schema.read_text(encoding='utf-8'))
statements = [part.strip() for part in attempt.read_text(encoding='utf-8').split(';') if part.strip()]
cursor = database.cursor()
for statement in statements[:-1]:
    cursor.execute(statement)
rows = cursor.execute(statements[-1]).fetchall()

print('Actual output:')
for row in rows:
    print(' '.join('NULL' if value is None else str(value) for value in row))
print()
print('Expected output:')
print(expected.read_text(encoding='utf-8').strip())
