
import logging
from typing import List

import requests


class Hitter:
    def __init__(self):
        ipfs_url = "http://ipfs.io/ipfs/"

    def hit(self, ids_file: str):
        with open(ids_file, "r") as ids:
            for id in ids:
                url = f"{self.ipfs_url}{id}"
                logging.info("Requesting %s", url)
                r = requests.get(url)
