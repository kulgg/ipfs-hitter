import sys

import fire
from exitstatus import ExitStatus

from ipfs_hitter.hitter import Hitter


def main():
    try:
        fire.Fire(Hitter)
    except Exception as exception:
        print(exception)
        sys.exit(ExitStatus.failure)

if __name__ == "__main__":
    main()
