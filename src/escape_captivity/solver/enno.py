import random
import string
import re
from urllib.parse import ParseResult

import httpx

from .base import BaseSolver



class EnnoSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc == "zgb.passengerwifi.com"

    def solve(self, portal_url: ParseResult) -> bool:
        # Request html of portal_url

        # Extract token from <input name="_token" type="hidden" value="PpxVgEQKymUXxefB3zHWPy8A1eXgBXNXlZKRIjTe">
        search_token = re.search(r'(?:<input)(?:[^>]*)(?:name=\"_token\")(?:[^>]*)(?:value=\")([^\"]*)(?:\">)')