
import logging
from typing import List


class Hitter:
    def hit(self, urls : List[str]):
        for url in urls:
            logging.info(url)

    def _jaiosd(self):
        pass
