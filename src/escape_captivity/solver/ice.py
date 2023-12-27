import random
import string
from urllib.parse import ParseResult

import httpx

from .base import BaseSolver


class IceSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc in [
            "login.wifionice.de",
            "wifi.metronom.de", # Metronom / Icomera AB
        ]

    def solve(self, portal_url: ParseResult) -> bool:
        # Generate some random CSRF token
        csrf_token = ''.join(random.choices(string.ascii_letters + string.digits, k=33))
        r = httpx.post(f"{portal_url.scheme}://{portal_url.netloc}/de/",
                          data={"login": "true", "CSRFToken": csrf_token}, cookies=dict(csrf=csrf_token),
                          follow_redirects=False)

        if r.status_code in [302, 200]:
            return True
        return False
