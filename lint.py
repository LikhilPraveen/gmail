import sys
from pylint import lint

THRESHOLD = 2
def my_func():
  run = lint.Run(['factorial.py'], do_exit=False)
  score = run.linter.stats["global_note"] 
    
 if __name__ == '__main__':
    my_func()
