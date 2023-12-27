from typing import Union

import httpx

detect_portal = "http://detectportal.firefox.com/canonical.html"


def get_captive_portal_address() -> Union[str, None]:
    """
    Function trying to determine address of captive portal.
    If captive portal is detected, the address is returned.
    Otherwise, None is returned.
    :return: Address of captive portal or None if no captive portal is detected.
    """
    try:
        response = httpx.get(detect_portal, follow_redirects=False, timeout=5)
        if response.status_code == 302:
            return response.headers.get("Location")
    except httpx.exceptions.RequestException:
        pass
    return None


def check_internet_connection() -> bool:
    """
    Check internet connectivity by trying to connect to the detect portal.
    :return: True if internet connection is available, False otherwise.
    """
    try:
        response = httpx.get(detect_portal, follow_redirects=False, timeout=5)
        if response.status_code == 200:
            return True
    except httpx.RequestError:
        pass
    return False

def is_behind_captive_portal() -> bool:
    pass
