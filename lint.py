import argparse
import logging
from pylint.lint import Run


logging.getLogger().setLevel(logging.INFO)

threshold = 5.0

logging.info('PyLint Starting | '
             'Path: {} | '
             'Threshold: {} '.format('factorial.py', threshold))

results = Run(['factorial.py'], do_exit=False)

final_score = results(['factorial.py'], exit=False).linter.stats.global_note

if final_score < threshold:

    message = ('PyLint Failed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.error(message)

else:
    message = ('PyLint Passed | '
               'Score: {} | '
               'Threshold: {} '.format(final_score, threshold))

    logging.info(message)

    exit(0)

