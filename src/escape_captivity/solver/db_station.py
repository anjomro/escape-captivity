import random
import string
from urllib.parse import ParseResult

import requests

from .base import BaseSolver


class DBStationSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc == "wifi.bahn.de"

    def solve(self, portal_url: ParseResult) -> bool:
        r = requests.post(f"{portal_url.scheme}://{portal_url.netloc}/login",
                          data={"oneSubscriptionForm_connect_policy_accept": "on", "login": "oneclick"},
                          follow_redirects=False, #allow unsafe tls
                          )
        if r.status_code in [302, 200]:
            return True
        return False

