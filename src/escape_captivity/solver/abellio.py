import random
import string
from urllib.parse import ParseResult

import httpx

from .base import BaseSolver


class AbellioSolver(BaseSolver):
    def applicable(self, portal_url: ParseResult) -> bool:
        return portal_url.netloc == "wasabi.hotspot-local.unwired.at"

    def solve(self, portal_url: ParseResult) -> bool:
        user_session_id = dict([x.split("=", 1) for x in  portal_url.query.split("&")]).get("user_session_id", "72957471-6354-4853-961f-9ab4dab4e69e")
        http2_client = httpx.Client(http2=True)
        r = http2_client.post(f"{portal_url.scheme}://{portal_url.netloc}/api/graphql", json={
        "operationName": "client_connect",
        "query": "mutation client_connect($userSessionId: ID!, $userAgentLang: String, $userAgentCountry: String, $input: ConnectInput, $widget_id: ID!, $code: String) {\n  client_connect(\n    user_session_id: $userSessionId\n    user_agent_lang: $userAgentLang\n    user_agent_country: $userAgentCountry\n    input: $input\n    widget_id: $widget_id\n    code: $code\n  ) {\n    user_session_id\n    time_start\n    state\n    error {\n      ...PolicyViolationError\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PolicyViolationError on Error {\n  error_code\n  error_message\n  current_value_bytes\n  max_value_bytes\n  current_value_seconds\n  max_value_seconds\n  __typename\n}",
        "variables": {
		"input": None,
		"userAgentCountry": None,
		"userAgentLang": None,
		"userSessionId": user_session_id,
		"widget_id": "2b8f4b13-a14f-4559-84ce-c2588058ddc0"
            }
        })
        if r.status_code in [200, 302]:
            return True
        return False
