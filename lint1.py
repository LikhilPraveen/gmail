import sys
from pylint import lint

THRESHOLD = 2

run = lint.Run(['factorial.py'], do_exit=False)
score = Run(['factorial.py'], exit=False).linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    
