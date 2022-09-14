import sys
import argparse
import logging
import Exception
from pylint.lint import Run


logging.getLogger().setLevel(logging.INFO)

threshold = 5.0

logging.info('PyLint Starting | '
             'Path: {} | '
             'Threshold: {} '.format('factorial.py', threshold))

final_score = Run(['factorial.py'], exit=False).linter.stats.global_note

logging.info(final_score)

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))
    raise Exception(message)
    logging.error(message)
    sys.exit(1)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))
    raise Exception(message)
    logging.info(message)

    exit(0)

