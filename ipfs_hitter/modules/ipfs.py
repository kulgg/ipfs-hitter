
import concurrent.futures
import logging

import requests


class Ipfs:
    def __init__(self):
        self.ipfs_url = "http://ipfs.io/ipfs/"

    def hit(self, ids_file: str):
        logging.info("Starting requesting ipfs urls")
        def _hit(url):
            logging.info("Requesting %s", url)
            r = requests.get(url)
            return r.status_code

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            futures = []
            with open(ids_file, "r") as ids:
                for id in ids:
                    url = f"{self.ipfs_url}{id}"
                    futures.append(executor.submit(_hit, url))

            for future in concurrent.futures.as_completed(futures):
                try:
                    logging.info(future.result())
                except requests.ConnectTimeout:
                    logging.exception("Connection timeout")
        logging.info("Finished requesting ipfs urls")
