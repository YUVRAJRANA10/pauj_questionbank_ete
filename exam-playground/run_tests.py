import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
status = 0
for topic in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('.') and p.name != '_solutions'):
    for qdir in sorted(p for p in topic.iterdir() if p.is_dir() and p.name.startswith('Q')):
        sol = qdir / 'Solution.java'
        if sol.exists():
            r = subprocess.run(['javac', 'Solution.java'], cwd=qdir, capture_output=True, text=True)
            if r.returncode != 0:
                print(f'{qdir.name}: compile failed')
                status = 1
if status == 0:
    print(f'Validated {sum(1 for p in root.iterdir() if p.is_dir() and p.name != "_solutions") } topics with Java stubs compiling successfully.')
raise SystemExit(status)
