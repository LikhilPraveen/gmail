import sys
from pylint import lint
from typing import TextIO
from pylint.lint import Run

THRESHOLD = 2
def my_func():
  default_stdout = sys.stdout
  sys.stdout = type("Dummy", (TextIO,), {"write": lambda self, data: ()})()
  score = Run(["./src"], exit=False).linter.stats.global_note
  sys.stdout = default_stdout
  print(score)
    
if __name__ == '__main__':
    my_func()
