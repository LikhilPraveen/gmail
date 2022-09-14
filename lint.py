import argparse
import logging
from pylint.lint import Run

logging.getLogger().setLevel(logging.INFO)

def my_func():
  threshold = 2.0

  results = Run(['factorial.py'], do_exit=False)

  final_score = results.linter.stats['global_note']

  if final_score < threshold:

      message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

      logging.error(message)
      raise Exception(message)

  else:
      message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

      logging.info(message)

      exit(0)
    
if __name__ == '__main__':
    my_func()
