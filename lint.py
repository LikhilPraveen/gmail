import sys
from pylint import lint

THRESHOLD = 2
def my_func():
  run = lint.Run(['factorial.py'], do_exit=False)
  score = Run([...], exit=False).linter.stats.global_note
  print(score)
    
if __name__ == '__main__':
    my_func()
