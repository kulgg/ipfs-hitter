import logging
import sys

import fire
from exitstatus import ExitStatus

from ipfs_hitter.hitter import Hitter


def configure_logging():
    log_format = "%(asctime)s [%(levelname)s] %(module)s.%(funcName)s(): %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)

def main():
    configure_logging()

    try:
        fire.Fire(Hitter)
    except Exception as exception:
        logging.exception(exception)
        sys.exit(ExitStatus.failure)

if __name__ == "__main__":
    main()
