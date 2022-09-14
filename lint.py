import sys
from pylint import lint

THRESHOLD = 2
def my_func():
  run = lint.Run(['factorial.py'], do_exit=False)
  score = run.linter.stats["global_note"] 

  if score < THRESHOLD:
     print("Linter failed: Score < threshold value")
     sys.exit(1)
    
 if __name__ == '__main__':
    my_func()
