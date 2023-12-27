import random
import string
from typing import Dict
from urllib.parse import ParseResult, urlparse
import re

import requests

from .base import BaseSolver


class DBRegioSouthEastSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc in ["hotsplots.de", "www.hotsplots.de"]

    def solve(self, portal_url: ParseResult) -> bool:
        query_parameters: Dict = dict([x.split("=", 1) for x in  portal_url.query.split("&")])
        r = requests.post(f"https://{portal_url.netloc}/{portal_url.path}",
                          data={
                                  "haveTerms": "1",
                                  "termsOK": "on",
                                  "button": "Jetzt+kostenlos+surfen",
                                  "challenge": query_parameters.get("challenge", ""),
                                  "uamip": query_parameters.get("uamip", ""),
                                  "uamport": query_parameters.get("uamport", ""),
                                  "userurl": "http://192.168.44.1/",
                                  "myLogin": "agb",
                                  "ll": "de",
                                  "nasid": query_parameters.get("nasid", ""),
                                  "custom": "1"
                              },
                          follow_redirects=False)

        if r.status_code in [200]:
            logon_url_matches = re.search(r'<meta http-equiv="refresh" content="0;url=(.*?)"', r.text)
            if logon_url_matches:
                #
                logon_url = logon_url_matches.group(1).replace("&amp;", "&")
                r2 = requests.get(logon_url, follow_redirects=False)
                if r2.status_code in [302, 200]:
                    return True
        return False
