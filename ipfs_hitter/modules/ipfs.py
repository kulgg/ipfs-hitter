
import asyncio
import concurrent.futures
import logging

import requests


class Ipfs:
    def __init__(self):
        self.ipfs_url = "http://ipfs.io/ipfs/"

    async def hit(self, ids_file: str, inverse_order: bool = False):
        logging.info("Starting requesting ipfs urls")
        def _hit(url):
            logging.info(url)
            try:
                r = requests.get(url, timeout=500)
                logging.info(r.status_code)
            except Exception as exception:
                logging.info("%s: exception", url)


        ids = open(ids_file, "r")
        urls = [f"{self.ipfs_url}{id}" for id in ids.read().split("\n")]
        ids.close()

        if inverse_order:
            urls.reverse()

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            loop = asyncio.get_event_loop()
            tasks = [loop.run_in_executor(executor, _hit, (url)) for url in urls]

            
            for response in await asyncio.gather(*tasks):
                pass
        logging.info("Finished requesting ipfs urls")
