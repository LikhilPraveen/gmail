import sys
import argparse
import logging
from pylint.lint import Run


logging.getLogger().setLevel(logging.INFO)

threshold = 8.0

logging.info('PyLint Starting | '
             'Path: {} | '
             'Threshold: {} '.format('factorial.py', threshold))

final_score = Run(['send.py'], exit=False).linter.stats.global_note

logging.info(final_score)

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))
    logging.error(message)
    sys.exit(1)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))
    logging.info(message)

    exit(0)

