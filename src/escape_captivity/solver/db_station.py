import random
import string
from urllib.parse import ParseResult

import requests

from .base import BaseSolver


class DBStationSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc == "wifi.bahn.de"

    def solve(self, portal_url: ParseResult) -> bool:
        pre_request = requests.get(f"{portal_url.scheme}://{portal_url.netloc}")
        if pre_request.url == 'https://wifi.bahn.de/cna/':
            # For DB-Regio / Süwex; Maybe a new general system?
            r = requests.post(f"{portal_url.scheme}://{portal_url.netloc}/cna/logon")
        else:
            r = requests.post(f"{portal_url.scheme}://{portal_url.netloc}/login",
                              data={"oneSubscriptionForm_connect_policy_accept": "on", "login": "oneclick"},
                              )
        if r.status_code in [302, 200]:
            return True
        return False

